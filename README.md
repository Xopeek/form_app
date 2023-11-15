# Django Form Validator

Простое Django-приложение для валидации форм.

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:Xopeek/form_app.git
```
2. Перейдите в каталог с проектом:
```bash
cd formvalid
```
3. Создайте виртуальное окружение:
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
4. Установите зависимости:
```bash
pip install -r requirements.txt
```
5. Создайте файл .env в корне проекта и добавьте необходимые переменные окружения (см. следующий раздел)

# Запуск
1. Заполните тестовыми данными:
```bash
python manage.py setup_test_data
```
2. Запустите сервер:
```bash
python manage.py runserver
```
3. Чтобы не делать запросы, добавлена команда. Откройте второй терминал, перейдите в корень проекта и выполните:
```bash
python manage.py test_request
```
# Конфигурация переменных окружения (.env)
В корне проекта создайте файл .env и укажите следующие переменные окружения:
```
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
```
Примечание: SECRET_KEY должен быть уникальным и сложным. Не используйте тот, что указан в примере.

# Как сделать свой запрос
На примере postman:
URL: http://127.0.0.1:8000/get_form/ POST
Body:
field_name=field_type

### field_name это название поля, field_type это тип поля который нужно отправить.
### Данные поля можно посмотреть в db.json

# Технологии
+ Python
+ Django
+ TinyDB

### Работу выполнил Семляков Игорь
