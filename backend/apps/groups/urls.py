from django.urls import path

from apps.groups.views import GroupListCreateView, GroupListUpdateModulesView, GroupListAddUsersView

urlpatterns = [
    path('', GroupListCreateView.as_view(), name='group_list_create'),
    path('/<int:pk>/modules', GroupListUpdateModulesView.as_view(), name='group_list_update_modules'),
    path('/<int:pk>/users', GroupListAddUsersView.as_view(), name='group_list_add_users'),
]
