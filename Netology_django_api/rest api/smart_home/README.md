# ДЗ по теме Docker с проектом django rest api
Установите Docker
Сделайте клон репозитория с проектом
Постройте образ Docker: docker build -t django-rest-api .
Запустите контейнер: docker run -p 8000:8000 django-rest-api
Сервер будет доступен по адресу: http://localhost:8000/api/sensors/