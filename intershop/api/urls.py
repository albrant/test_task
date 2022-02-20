from django.urls import include, path
from rest_framework import routers

from .views import GoodsViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('goods', GoodsViewSet, basename='goods')
#router.register(r'goods/(?P<group_id>\d+)/',GoodsViewSet, basename='goods')

urlpatterns = [
    path('v1/', include(router.urls)),
]