from tokenize import group
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Goods

User = get_user_model()


class GoodsModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='TEST_GROUP_SLUG',
            description='Тестовое описание',
        )
        cls.goods = Goods.objects.create(
            article = 'TEST001',
            caption = 'Test_goods',
            quantity = 1000
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        goods = GoodsModelTest.goods
        str_goods = str(goods)
        expected_string = goods.caption[:20]
        self.assertEqual(str_goods, expected_string)
        group = GoodsModelTest.group
        str_group = str(group)
        expected_string = group.title
        self.assertEqual(str_group, expected_string)

    def test_title_help_text(self):
        goods = GoodsModelTest.goods
        help_text = goods._meta.get_field('caption').help_text
        self.assertEqual(help_text, 'Введите название товара')
        group = GoodsModelTest.group
        help_text = group._meta.get_field('title').help_text
        self.assertEqual(help_text, 'Выберите группу')
