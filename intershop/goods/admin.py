from django.contrib import admin

from .models import Goods, Group


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'caption', 'group', 'quantity', 'price')
    search_fields = ('atricle', 'caption', 'group')
    list_filter = ('group',)
    empty_value_display = '-пусто-'
    list_editable = ('group', 'quantity', 'price')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Group)