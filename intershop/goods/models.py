from django.contrib.auth import get_user_model
from django.db import models
from django.forms import BooleanField

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Goods(models.Model):
    article = models.CharField(max_length=50)
    caption = models.TextField()
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="goods", blank=True, null=True
    )
    quantity = models.FloatField() 
    # либо кол-во нужно выносить в отдельную сущность - приход на склад
    price = models.FloatField()
    
    def __str__(self):
        return self.caption


class Order(models.Model):
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    description = models.TextField()
    is_done = models.BooleanField()


class GoodsInOrder(models.Model):
    added = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='goods_in_order'
    )
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, related_name='goods_in_order'
    )
    quantity = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'goods'],
                name='unique_order_goods'
            )
        ]

    def __str__(self) -> str:
        return self.goods.caption