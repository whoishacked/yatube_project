# Yatube
## Описание
Yatube – cоциальная сеть, разработанная на фреймворке Django. Пользователям доступен личные кабинет с авторизацией. Можно подписываться на интересных авторов. Авторы могут создавать различные произведения, выбирая жанры из предложенного списка.
## Установка
Клонируем репозиторий:
```
git clone https://github.com/whoishacked/yatube_project/
```

Переходим в папку с проектом:
```
cd yatube_project
```

Устанавливаем и активируем venv:
```
python3 -m venv venv
```

```
source venv/bin/activate
```

Устанавливаем pip:
```
python3 -m pip install --upgrade pip
```

Устанавливаем зависимости:
```
pip install -r requirements.txt
```

Создаем миграции:
```
python manage.py makemigrations
```

Выполняем миграции:
```
python manage.py migrate
```

Запускаем проект:
```
python3 manage.py runserver
```

Проект будет доступен по адресу:
```http://127.0.0.1:8000/```

## Технологии
**Python 3.7**
**Django 2.2.19**

Полный список доступен в **requirements.txt**

## Об авторах
**Кутузов Андрей:**
- Telegram: @andrewkutuzov
- Email: britvill@gmail.com
