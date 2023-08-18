from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.dataclasses.user_dataclass import User
from core.permissions.is_manager import IsManager
from core.permissions.is_super_user_or_manager_read_only_permission import IsSuperUserOrManagerReadOnly
from core.permissions.is_superuser import IsSuperUser

from apps.courses.models import CourseModel, CourseNameModel
from apps.courses.serializers import (
    CourseAddUsersSerializer,
    CourseNameSerializer,
    CourseSerializer,
    CourseUpdateModulesSerializer,
)
from apps.modules.serializers import ModuleSerializer
from apps.users.serializers import UserResponseSerializer, UserSerializer


class CourseNamesListCreateView(ListCreateAPIView):
    """
    get:
        Get list of course names
    post:
        Create new course name
    """
    serializer_class = CourseNameSerializer
    queryset = CourseNameModel.objects.all()
    permission_classes = (IsSuperUserOrManagerReadOnly,)


class CoursesListCreateView(ListCreateAPIView):
    """
    get:
        Get list of courses
    post:
        Create course and add modules from last course
    """
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = (IsManager,)


class CourseListUpdateModulesView(GenericAPIView):
    """
    get:
        List of modules by course id
    patch:
        Add modules by course id
    """
    serializer_class = CourseUpdateModulesSerializer
    queryset = CourseModel.objects.all()
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


class CourseListAddUsersView(GenericAPIView):
    # todo pagination, comment and doc
    queryset = CourseModel.objects.all_with_users()

    def get(self, *args, **kwargs):
        course = self.get_object()
        serializer = UserSerializer(course.users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        course = self.get_object()
        serializer = CourseAddUsersSerializer(data=data, context={'course': course}, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = CourseSerializer(course)
        return Response(serializer.data, status.HTTP_201_CREATED)
