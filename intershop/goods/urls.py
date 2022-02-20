from django.urls import include, path

from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name='index'),
    path('busket/', views.busket, name='busket'),
    path('goods/<int:goods_id>/add/',views.goods_add_to_busket, name='add'),
    path('goods/<int:goods_id>/delete/',views.goods_delete_from_busket, name='delete'),
    path('order/<int:order_id>/apply/', views.order_apply, name='order_apply'),
]
