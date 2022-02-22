from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from goods.models import Group, Goods

from .serializers import GoodsSerializer, GroupSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('group',)
    search_fields = ('caption',)


class GroupSerializer(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
