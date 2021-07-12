from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', include('mainapp.urls')),
    path('basket/', include('basketapp.urls', namespace='basketapp')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)