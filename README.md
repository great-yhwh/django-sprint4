# Blogicum — Спринт 4

Учебный проект на Django: блог-платформа с системой аутентификации, пагинацией,
комментариями, загрузкой изображений и кастомными страницами ошибок.

<!-- TOC -->
* [Blogicum — Спринт 4](#blogicum--спринт-4)
  * [Стек](#стек)
  * [Установка и запуск](#установка-и-запуск)
    * [1. Получение кода из предыдущего спринта](#1-получение-кода-из-предыдущего-спринта)
    * [2. Подготовка шаблонов](#2-подготовка-шаблонов)
    * [3. Виртуальное окружение и зависимости](#3-виртуальное-окружение-и-зависимости)
    * [4. Миграция, фикстура, статика](#4-миграция-фикстура-статика)
    * [5. Запуск](#5-запуск)
    * [6. Тесты](#6-тесты)
  * [Структура](#структура)
<!-- TOC -->

## Стек

- Python 3.10+
- Django 4.x
- SQLite (по умолчанию)
- pytest / django-pytest


## Установка и запуск

### 1. Получение кода из предыдущего спринта

```bash
git remote add django_sprint3 https://github.com/<username>/django_sprint3.git
git fetch django_sprint3
git checkout django_sprint3/main -- blogicum
git remote remove django_sprint3
```

### 2. Подготовка шаблонов

```bash
rm -rf blogicum/templates
mv templates blogicum/
```

### 3. Виртуальное окружение и зависимости

```bash
python3 -m venv .venv
source .venv/bin/activate   
pip install -r requirements.txt
```

### 4. Миграция, фикстура, статика

```bash
cd blogicum
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ../db.json
python manage.py collectstatic --noinput
```

### 5. Запуск

```bash
python manage.py createsuperuser   # по желанию
python manage.py runserver
```

Сайт доступен по адресу **<http://127.0.0.1:8000/>**

### 6. Тесты

```bash
cd ..
pytest
```

## Структура

```
django_sprint4/
├── blogicum/
│   ├── blog/          # приложение «Блог»
│   ├── pages/         # статичные страницы
│   ├── templates/     # все шаблоны проекта
│   ├── manage.py
│   └── blogicum/      # конфигурация проекта
├── tests/             # тесты
├── db.json            # фикстура
├── requirements.txt
└── README.md
```