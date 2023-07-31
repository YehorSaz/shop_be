from rest_framework.generics import ListCreateAPIView

from core.permissions.is_manager import IsManager
from core.permissions.is_super_user_or_manager_read_only_permission import IsSuperUserOrManagerReadOnly

from apps.courses.models import CourseModel, CourseNameModel
from apps.courses.serializers import CourseNameSerializer, CourseSerializer


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
        Create course
    """
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = (IsManager,)
