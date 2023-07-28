from django.urls import path

from apps.admin.views import ManagerListCreateView, MentorListCreateView

urlpatterns = [
    path('/managers', ManagerListCreateView.as_view(), name='admin_managers_list_create'),
    path('/mentors', MentorListCreateView.as_view(), name='admin_mentors_list_create')
]
