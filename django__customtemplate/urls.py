from django.contrib import admin
from django.urls import path, include
# project/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# from django.conf.urls.static import static
# from django.conf import settings
# # serve static files and media
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


