from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .yasg import schema_view

swagger_urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

api_auth_urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]

api_urlpatterns = [
    path('schema/', include(swagger_urlpatterns)),
    path('auth/', include(api_auth_urlpatterns)),
    # path('accounts/', include('apps.accounts.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
