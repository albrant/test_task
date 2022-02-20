from rest_framework import filters, viewsets

from goods.models import Group, Goods

from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

    #def get_queryset(self):
    #    group_id = self.kwargs.get('group_id')
    #    group = get_object_or_404(Group, id=group_id)
    #    return group.goods.all()