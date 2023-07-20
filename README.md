# Проверка доступности сайта  

### Стек:  
- Python  
- Django  
- Django-jazzmin
- Celery  
- Celery-beat  
- Redis  
- RebbitMQ  


## Запуск проекта
1. Клонировать репозиторий:  
```git clone https://github.com/AleksSpace/Django_check_urls.git```
2. Перейти в директорию в которую клонировали репозиторий и ввести команду для сборки и запуска проекта:  
```docker-compose up -d```
3. Ввести команду для запуска миграций  
```docker-compose run django python manage.py makemigrate```  
```docker-compose run django python manage.py migrate```  
4. Создать суперпользователя:  
```docker-compose run django python manage.py createsuperuser```  
 - Далее нужно будет ввести любое имя латинице
 - Email можете вводить или пропустить нажав Enter  
 - Ввести пароль
 - Подтвердить пароль
5. Переходим по адресу  http://localhost:8000/admin  
6. Вводим логин и пароль которые создали ранее
7. Слева нажимаем на Urls и добавляем url
8. Слева во вкладке Task results появятся выполненные Tasks
9. Заходим в check_url.tasks.check_url и во вкладке Result будет видно какие url доступны. Данные обновляются каждую минуту.


