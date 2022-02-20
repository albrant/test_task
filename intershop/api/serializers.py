from rest_framework import serializers

from goods.models import Goods, Group


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'

    
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')
