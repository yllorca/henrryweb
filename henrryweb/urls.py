from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    urlpatterns += url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),