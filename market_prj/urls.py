from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('', mainapp.main, name='main'),
    path('list_of_accommodations/', include('mainapp.urls', namespace='acc')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
