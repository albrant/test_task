from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Интернет-магазин Альбранта Е.О.'
admin.site.index_title = 'Админка'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),    
    path('', include('goods.urls', namespace='goods')),
    #path('verify/', include('verification.urls')),
    path('api/', include('api.urls', namespace='api')),
]
