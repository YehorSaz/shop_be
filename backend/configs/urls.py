from django.urls import include, path

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='BigBirdLMS',
        default_version='v1',
        description='Learning Management System for Okten School',
        contact=openapi.Contact(email='demchyshyn.v87@gmail.com')
    ),
    public=True,
    permission_classes=[AllowAny]
)
urlpatterns = [
    path('api/auth', include('apps.auth.urls')),
    path('api/admin', include('apps.admin.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0)),
]
