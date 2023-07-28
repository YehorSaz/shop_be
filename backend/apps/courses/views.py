from rest_framework.generics import ListCreateAPIView

from core.permissions.is_manager import IsManager

from apps.courses.models import CourseModel
from apps.courses.serializers import CourseSerializer


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
