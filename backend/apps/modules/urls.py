from django.urls import path

from apps.modules.views import ModulesListCreateView

urlpatterns = [
    path('', ModulesListCreateView.as_view(), name='modules_list_create')
]
