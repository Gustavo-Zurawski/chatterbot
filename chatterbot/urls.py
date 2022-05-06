from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from chatterbot.api.urls.v1 import router
from chatterbot.views import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
      title="Chatter Bot API",
      default_version='v1',
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', index, name='index'),
    path('api/v1/', include((router.urls, 'bond'), namespace='apiv1'), name='apiv1'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
