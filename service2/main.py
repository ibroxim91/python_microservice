# service2/app/main.py
import pika
import asyncio
from fastapi import FastAPI
import telebot 
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN', None)

bot = telebot.TeleBot(TOKEN)


app = FastAPI()
@app.get('/')
def main():
    return {'message': 'Service 2 is running'}

async def send_email(body: str):
    print("Xabar emailga jo‘natildi:", body)
    bot.send_message(-1001234567890, body )

def callback(ch, method, properties, body):
    asyncio.run(send_email(body.decode('utf-8')))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='service_queue')
    channel.basic_consume(queue='service_queue', on_message_callback=callback, auto_ack=True)
    print('Xabarlar kutilyapti...')
    channel.start_consuming()

@app.on_event("startup")
async def startup_event():
    # Xabarlar iste'molini asinxron boshlash
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, start_consumer)
