import datetime

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
        help_text='Выберите группу')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ['title']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'    

    def __str__(self):
        return self.title

# слово goods означает как товар, так и товары
class Goods(models.Model):
    article = models.CharField(
        max_length=20,
        verbose_name='Артикль',
        help_text='Введите артикль товара'        
    )
    caption = models.CharField(
        max_length=30,
        verbose_name='Название товара',
        help_text='Введите название товара'         
    )
    group = models.ManyToManyField(Group)
    quantity = models.IntegerField(default=1)
    # в идеале нужно выносить количество товара в отдельную структуру
    # рассчитывая приход на склад, продажу со склада,
    # для данного проекта это упростим - будет просто количество товара
    price = models.FloatField(default=100)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.caption[:20]


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    is_done = models.BooleanField(
        default=False,
        verbose_name='Выполнен'
    )
    order_date = models.DateTimeField(
        'Дата заказа',
        auto_now_add=True
    )
    
    def __str__(self):
        return f'Заказ № {self.id} от {self.order_date}'


# связь "многие-ко-многим" здесь не получится использовать, т.к. 
# для каждого товара нужно указывать его количество в заказах
class GoodsInOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='goods_in_order'
    )
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, related_name='goods_in_order'
    )
    quantity = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'goods'],
                name='unique_order_goods'
            )
        ]

    def __str__(self):
        return self.goods.caption
