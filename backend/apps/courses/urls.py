from django.urls import path

from apps.courses.views import CourseListUpdateModulesView, CourseNamesListCreateView, CoursesListCreateView

urlpatterns = [
    path('', CoursesListCreateView.as_view(), name='courses_list_create'),
    path('/names', CourseNamesListCreateView.as_view(), name='course_names_list_create'),
    path('/<int:pk>/modules', CourseListUpdateModulesView.as_view(), name='course_list_update_modules'),
]
