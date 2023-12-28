#  Cars
## REST API 

### 1. Создание и развертывание контейнеров проекта:

Форкнуть репозиторий, склонировать и перейти в корень папки `api_cars`

Переименовать .env.example в .env и заполнить своими данными по шаблону:

```bash
mv .env.example .env
nano .env
```

Убедиться, что сервис (демон) Docker активен в системе:

```bash
sudo systemctl status docker
```

Развернуть контейнерное пространство:

(!) если развертка происходит впервые:

- необходимо открыть docker-compose.yml и заменить для каждого из контейнеров `backend`, `gateway` способ выбора образа с `image` на `build` - таким образом будут созданы исходные docker образы проекта
- далее возможно создать свои образы `backend`, `gateway` и использовать параметр `image`

```bash
nano docker-compose.yml
```
```
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

## Запуск проекта 
### Заполнить в настройках репозитория секреты .env, необходимы для работы postgres в docker 
 
```python 
POSTGRES_DB=db_name # Задаем имя для БД. 
POSTGRES_USER=username # Задаем пользователя для БД. 
POSTGRES_PASSWORD=password # Задаем пароль для БД. 
DB_HOST=db 
DB_PORT=5432 
``` 
 
### Далее в папке api_cars выполняем команду: 
 
```bash 
sudo docker compose -f docker-compose.production.yml up -d --build 
``` 
 
 
### Для доступа к контейнеру backend и сборки финальной части выполняем следующие команды: 
 
```bash 
docker-compose exec backend python manage.py makemigrations 
``` 
 
```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```
## Примеры работы программы:
### Вывод всех автомобилей со средним рейтингом
![image](https://github.com/FILL9214/api_cars/assets/97111713/d04e21a3-e6e5-4550-928d-334deb0008a3)

### Вывод популярных автомобилей
![image](https://github.com/FILL9214/api_cars/assets/97111713/d4be43b2-a5e4-4192-b243-be9c480437d8)
### Добавление оценки автомобилю
![image](https://github.com/FILL9214/api_cars/assets/97111713/ef6a5146-7859-4a9b-ac58-c8b857bcacba)

### Создание автомобиля, при условии его нахождения в базе по URL https://vpic.nhtsa.dot.gov/api/
![image](https://github.com/FILL9214/api_cars/assets/97111713/af37f8b2-a98d-497c-b476-c6ac5ca988b0)

![image](https://github.com/FILL9214/api_cars/assets/97111713/c7f3bc9f-bc7a-4e2f-9519-f1498434c8d8)


### Автор
Филипп Истомин
