#  Интернет-магазин InterShop
Данный проект выполнен как тестовое задание, поэтому не несёт в себе реально действующего функционала.
Сервис позволяет заходить на страницу товаров, добавлять товары себе в корзину, выполнять эмуляцию оплаты.
Для пользователя реализован основной функционал: регистрация, аутентификация, смена пароля и т.д.

Неавторизованный пользователь может смотреть список товаров. Авторизованный может заходить в свою корзину, 
добавлять в неё товары, либо удалять товары оттуда.

#  Запуск проекта
Для запуска проекта необоходимо выполнить следующие действия:

установка зависимостей
pip install -r requirements

применение миграций, создание БД SQLite
python manage.py makemigrations
python manage.py migrate

создание польователя-админа системы
python manage.py createsuperuser

запуск сервера разработчика
python manage.py runserver
