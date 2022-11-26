import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://kdtbtirf:ZMAfLPaKnBnwKR0oYFY3odqTNhxl_BZo@jackal.rmq.cloudamqp.com/kdtbtirf')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='matriz')

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('matriz',
                      callback,
                      auto_ack=True)

print(' [*] Esperando por roupas:')
channel.start_consuming()
connection.close()