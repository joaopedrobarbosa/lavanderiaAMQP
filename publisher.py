import pika, os, time

url = os.environ.get('CLOUDAMQP_URL', 'amqps://kdtbtirf:ZMAfLPaKnBnwKR0oYFY3odqTNhxl_BZo@jackal.rmq.cloudamqp.com/kdtbtirf')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='matriz')
x = 1
while True:
    try:
        channel.basic_publish(exchange='',
                            routing_key='matriz',
                            body='Roupa para lavar ' + str(x))
        print(" [x] Sent 'Roupa Enviada com Sucesso'")
        x = x + 1
        time.sleep(5)
    except KeyboardInterrupt:
        connection.close()