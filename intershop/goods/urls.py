from django.urls import include, path

from . import views


app_name = 'goods'


urlpatterns = [
    path('', views.index, name='index'),
    path('busket/', views.busket, name='busket'),
]
