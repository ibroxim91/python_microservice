# service2/Dockerfile
FROM python:3.9-slim

# Netcat o'rnatish uchun mos paketni o'rnatish
# RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

WORKDIR /app
COPY . /app

# RUN chmod +x wait-for-it.sh

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
