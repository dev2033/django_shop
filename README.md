Репозиторий интернет-магазина на Django 3.

Установка (для пользователей операционных систем семейства **MacOs/Linux**):

1. Открыть терминал или консоль и перейти в нужную Вам директорию
2. Прописать команду `https://github.com/dev2033/django_project_shop.git`
3. Прописать следующие команды:
    - `python3 -m venv ДиректорияВиртуальногоОкружения`
    - `source ДиректорияВиртуальногоОкружения/bin/activate`
4.  Перейти в директорию **django_project_shop/shop**
    - `pip install -r requirements.txt`
    - `python manage.py migrate`
5. Запустить сервер - `python manage.py runserver`
6. Не забудьте очистить директорию **media**. Она нужна для сохранения изображений товара
