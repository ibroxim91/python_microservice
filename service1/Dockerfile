# service1/Dockerfile
FROM python:3.9-slim
WORKDIR /app

# requirements.txt faylini konteynerga ko'chiramiz
COPY requirements.txt /app/
# Django ilovasini ko'chirish
COPY . /app/

# Kutubxonalarni o'rnatish
RUN pip install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
