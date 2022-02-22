from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.core.cache import cache

from ..models import Group, Goods


USERNAME = 'Test user'

User = get_user_model()


class GoodsURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестоая группа',
            slug='Слаг'
        )
        cls.goods = Goods.objects.create(
            article='TEST002',
            caption='Test_goods',
            quantity=10
        )

    def setUp(self):
        self.user = User.objects.create_user(username='HasNoName')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_add_url_redirect_anonymous(self):
        """Страница добавления товара в корзину /add/ перенаправляет анонимного пользователя."""
        response = self.client.get('/goods/1/add/', follow=True)
        self.assertRedirects(response, ('/auth/login/?next=/goods/1/add/'))

    def test_add_url_redirect_anonymous(self):
        """Попытка перехода в корзину /busket/ для анонимного пользователя заканчивается ошибкой 404."""
        response = self.client.get('/busket/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_access_pages_from_guest_users(self):
        """Анонимный пользователь может зайти на некоторые страницы (список товаров, логин и регистрация"""
        goods_id = GoodsURLTests.goods.pk
        url_names = (
            '/',
            '/auth/login/',
            '/auth/signup/',
        )
        for address in url_names:
            with self.subTest(address=address):
                response = self.client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_unexisting_page_get_404(self):
        response = self.client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_access_pages_from_authorized_users(self):
        goods_id = GoodsURLTests.goods.pk
        url_names = (
            '/',
            '/busket/',
            '/auth/login/',
            '/auth/signup/',            
        )
        for address in url_names:
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        goods_id = GoodsURLTests.goods.pk
        templates_url_names = {
            '/': 'goods/index.html',
            '/busket/': 'goods/busket.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)
