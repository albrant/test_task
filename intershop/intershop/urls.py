from django.contrib import admin
from django.urls import path, include
from django_otp.admin import OTPAdminSite
  
admin.site.__class__ = OTPAdminSite
admin.site.site_header = 'Интернет-магазин Альбранта Е.О.'
admin.site.index_title = 'Админка'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),    
    path('', include('goods.urls', namespace='goods')),
    path('api/', include('api.urls', namespace='api')),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
