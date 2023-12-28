#  Cars
## REST API 

### 1. Создание и развертывание контейнеров проекта:

Форкнуть репозиторий, склонировать и перейти в корень папки `api_cars`

Переименовать .env.example в .env и заполнить своими данными по шаблону:

```
mv .env.example .env
nano .env
```

Убедиться, что сервис (демон) Docker активен в системе:

```
sudo systemctl status docker
```

Развернуть контейнерное пространство:

(!) если развертка происходит впервые:

- необходимо открыть docker-compose.yml и заменить для каждого из контейнеров `backend`, `gateway` способ выбора образа с `image` на `build` - таким образом будут созданы исходные docker образы проекта
- далее возможно создать свои образы `backend`, `gateway` и использовать параметр `image`

```
nano docker-compose.yml
```
```
....
backend:
   ...
   # эту строку ниже:
   image: <username>/kittygram_backend
   # заменить на:
   build: ./backend/
   ...
gateway:
   ...
   # эту строку ниже:
   image: <username>/kittygram_gateway
   # заменить на:
   build: ./nginx/
   ...
```

Развернуть контейнерную группу в виде фоновоного демона:

```
docker compose up -d
```

Настроить миграции backend:

```
docker compose exec backend python manage.py migrate
```

Передать статику в Nginx:

```
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /kittygram/collect_static/. /backend_static/static/
```

Настроить сервер на отпраку запросов к сайту Cars на порт 8000 (согласно настройке образа `gateway`).

### Автор

Филипп Истомин