from django.urls import path

from apps.courses.views import CourseListCreateView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course_names_list_create'),
]
