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










