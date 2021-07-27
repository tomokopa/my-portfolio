# basic_code
from django.contrib import admin
from django.urls import path, include
# django_summernote
from django.conf import settings
from django.conf.urls.static import static

ADMIN_NO = settings.ADMIN_NO

# basic_code + django_summernote
urlpatterns = [
    path('admin/' + ADMIN_NO + '/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),
]

# django_summernote
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)