from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Group, Goods

User = get_user_model()


class GoodsPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Слаг'
        )
        cls.goods = Goods.objects.create(
            article='TEST004',
            caption='Тестовый товар',
            quantity=100
        )

    def setUp(self):
        self.user = User.objects.create_user(username='HasNoName')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        goods_id = GoodsPagesTests.goods.pk
        templates_pages_names = {
            reverse('goods:index'): 'goods/index.html',
            reverse('goods:busket'): 'goods/busket.html',
            reverse('goods:order_apply', kwargs={'order_id': '1'}):
                'goods/apply.html',
        }
        for reverse_name, template in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
