from django.urls import path

from apps.auth.views import MeView, TokenPairView, TokenRefreshView, UserActivateView, UserActivationRequestView

urlpatterns = [
    path('', TokenPairView.as_view(), name='auth_login'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<int:pk>', UserActivationRequestView.as_view(), name='auth_user_activation_request'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='auth_user_activate'),

]
