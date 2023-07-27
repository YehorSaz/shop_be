from django.urls import path

from .views import (
    ManagerActivateRecoveryPasswordView,
    ManagerActivationRecoveryPasswordRequestView,
    ManagerListCreateView,
)

urlpatterns = [
    path('/managers', ManagerListCreateView.as_view(), name='admin_managers_list_create'),
    path(
        '/managers/<int:pk>/activate_recovery',
        ManagerActivationRecoveryPasswordRequestView.as_view(),
        name='admin_managers_activate_recovery_token'
    ),
    path(
        '/managers/activate_recovery/<str:token>',
        ManagerActivateRecoveryPasswordView.as_view(),
        name='admin_managers_activate_recovery'
    )
]
