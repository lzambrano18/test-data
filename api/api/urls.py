import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from api.views import SwaggerSchemaView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('data.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^', SwaggerSchemaView.as_view())
]
