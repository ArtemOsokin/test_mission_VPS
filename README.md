## Проект тестового задания
Проект написан с использованием:
- Django REST-framework
- PostgreSQL

Запуск производиться через:
- Docker Compose
- nginx

### Запуск проекта

Осуществляется с помощью docker-compose. 

**`docker-compose up -d --build`**

После первой сборки требуется выполнить поочерёдно несколько команд:

1. Выполнить миграции
- `docker-compose exec web python manage.py migrate`

2. Выкатить статику проекта:

`docker-compose exec web python manage.py collectstatic  --noinput`

### API VPS CRUD

1. Создание VPS

**`api/v1/vps/create`**

2. Получить VPS по uid:

**`api/v1/vps/detail/<uuid:pk>`**

2. Получить список VPS с возможностью фильтрации:

**`api/v1/all`**