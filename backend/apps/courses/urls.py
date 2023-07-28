from django.urls import path

from apps.courses.views import CoursesListCreateView

urlpatterns = [
    path('', CoursesListCreateView.as_view(), name='courses_list_create')
    
]

