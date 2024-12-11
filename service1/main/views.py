import pika
from django.http import HttpResponse
from django.views import View

class SubmitFormView(View):
    def get(self, request):
        # Shakldan ma'lumotlarni olish
        data = request.GET.get('data', 'Data not send')

        # RabbitMQ bilan ulanish
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        # Navbat va xabarni yaratish
        channel.queue_declare(queue='service_queue')
        channel.basic_publish(exchange='', routing_key='service_queue', body=data)
        
        connection.close()
        return HttpResponse("Ma'lumot yuborildi!")
