from rest_framework.generics import ListCreateAPIView

from apps.courses.models import CourseModel
from apps.courses.serializers import CourseSerializer

from core.permissions.is_super_user_or_manager_read_only_permission import IsSuperUserOrManagerReadOnly


class CourseListCreateView(ListCreateAPIView):
    """
    get:
        Get list of course names
    post:
        Create new course name
    """
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = (IsSuperUserOrManagerReadOnly,)
