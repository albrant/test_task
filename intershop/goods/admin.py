from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Goods, Group


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


class GoodsInOrderAdmin(admin.ModelAdmin):    
    list_display = "__all__"


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Group)
