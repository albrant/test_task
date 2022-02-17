from django.urls import include, path
from rest_framework import routers

from .views import ShopViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'shop', ShopViewSet, basename='shop')


urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]