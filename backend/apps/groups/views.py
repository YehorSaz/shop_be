from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.groups.models import GroupModel
from apps.groups.serializers import GroupSerializer, GroupUpdateModulesSerializer, GroupAddUsersSerializer
from apps.modules.serializers import ModuleSerializer
from apps.users.serializers import UserSerializer
from core.permissions.is_manager import IsManager
from core.permissions.is_superuser import IsSuperUser


class GroupListCreateView(ListCreateAPIView):
    """
    get:
        Get list of groups
    post:
        Create group and add modules from last group
    """
    serializer_class = GroupSerializer
    queryset = GroupModel.objects.all()
    permission_classes = (IsManager,)


class GroupListUpdateModulesView(GenericAPIView):
    """
    get:
        List of modules by group id
    patch:
        Add modules by group id
    """
    serializer_class = GroupUpdateModulesSerializer
    queryset = GroupModel.objects.all()
    permission_classes = (IsSuperUser,)

    @swagger_auto_schema(responses={200: ModuleSerializer(many=True)})
    def get(self, *args, **kwargs):
        course = self.get_object()
        serializer = ModuleSerializer(course.modules, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: ModuleSerializer(many=True)})
    def patch(self, *args, **kwargs):
        course = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance=course, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = ModuleSerializer(course.modules, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class GroupListAddUsersView(GenericAPIView):
    """
        get:
            get course users by course id
        post:
            save users to course by course id
    """
    queryset = GroupModel.objects.all_with_users()
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        group = self.get_object()
        response = self.get_paginated_response(self.paginate_queryset(UserSerializer(group.users, many=True).data))
        return response

    @swagger_auto_schema(request_body=GroupAddUsersSerializer(many=True), responses={201: GroupSerializer()})
    def post(self, *args, **kwargs):
        data = self.request.data
        group = self.get_object()
        serializer = GroupAddUsersSerializer(data=data, context={'course': group}, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = GroupSerializer(group)
        return Response(serializer.data, status.HTTP_201_CREATED)
