# Diplom_todolist
дипломная работа
Coursework #7

#активация окружения diplom-env
source diplom-env/bin/activate  

#создание superuser
python3 manage.py createsuperuser 

#создание базы в docker
docker run --name Todolist_Alex -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
#docker run --name Todolist_Alex -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d todolist


#отключение docker
docker-compose down  

#миграции
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 

#удаление миграций
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete 

#посмотреть оригинальный путь
pwd

#распаковка docker-compose:
docker-compose up --build 

#установка зависимостей:
pip3 install -r requirements.txt  

#клон репозитория, из куросвой 6
git clone https://github.com/skypro-008/coursework_6_skymarket.git

python3 manage.py collectstatic  

#загрузка всех фикстур
python3 manage.py loadall

#загрузка конкретной фиктсуры:
python3 manage.py loaddata fixtures/comments.json 


# Посмотреть созданные volume
docker volume ls
# Создать volume
docker volume create
# Посмотреть детальную информацию
docker volume inspect <название volume> 
# Удалить volume
docker volume rm <название volume> 
# Удалить все не используемые в данный момент volume
docker volume prune 

# Проброс volume в контейнер
docker volume create test
docker run -v test:/dir_in_container <образ>
# Название volume–^ ^–Название директории внутри контейнера

# Проброс директории с хоста в контейнер
docker run -v /host_dir:/dir_in_container -d nginx
# Абсолютный путь до папки–^              ^-директория внутри контейнера

# Запустить всё приложение (контейнеры, сети и т. д.)
docker-compose up
# То же самое, только в режиме демона
docker-compose up -d
# Остановить контейнеры
docker-compose stop
# Запустить контейнеры
docker-compose start
# Остановить контейнеры и удалить все компоненты
docker-compose down
# Собрать необходимые образы, но ничего не запускать
docker-compose build
# Скачать необходимые образы
docker-compose pull
# Посмотреть логи сервисов
docker-compose logs

#просмотр 







