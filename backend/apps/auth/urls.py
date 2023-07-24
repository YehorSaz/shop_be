from django.urls import path

from apps.auth.views import RegisterView

from .views import MeView, TokenPairView, TokenRefreshView

urlpatterns = [
    path('', TokenPairView.as_view(), name='auth_login'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', RegisterView.as_view(), name='auth_register')

]
