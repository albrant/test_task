from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Goods, GoodsInOrder, Group, Order


class GoodsResource(resources.ModelResource):

    class Meta:
        model = Goods
        #fields = ('id', 'article', 'caption', 'quantity', 'price')


class GoodsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'article', 'caption', 'quantity', 'price')
    search_fields = ('atricle', 'caption', 'group')
    list_filter = ('group',)
    empty_value_display = '-пусто-'
    list_editable = ('quantity', 'price')
    filter_horizontal = ('group',)    
    resource_class = GoodsResource


class GoodsInOrderResource(resources.ModelResource):

    class Meta:
        model = GoodsInOrder


class GoodsInOrderAdmin(ImportExportModelAdmin):    
    list_display = ('id', 'goods', 'order',
                    'order_datetime', 'quantity',
                    'price', 'done')
    resource_class = GoodsInOrderResource
    
    def order_datetime(self, obj):
        return Order.objects.get(id=obj.order_id).order_date

    def price(self, obj):
        result = Goods.objects.get(id=obj.goods_id)
        return result.price
    
    def done(self, obj):
        return Order.objects.get(id=obj.order_id).is_done


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    empty_value_display = '-пусто-'

    
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GoodsInOrder, GoodsInOrderAdmin)
