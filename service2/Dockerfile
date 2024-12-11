# service2/Dockerfile
FROM python:3.9-slim
WORKDIR /app

# requirements.txt faylini konteynerga ko'chiramiz
COPY requirements.txt /app/

# FastAPI ilovasini ko'chirish
COPY . /app/

# Kutubxonalarni o'rnatish
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
