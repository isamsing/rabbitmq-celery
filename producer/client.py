import pika
import sys


def send_message(msg: str):
    with pika.BlockingConnection(
        pika.ConnectionParameters(credentials=pika.PlainCredentials('user', 'password'),
                                  host='localhost')) as connection:
        channel = connection.channel()

        # channel.queue_declare(queue='default', durable=True)
        channel.queue_bind(queue='default',
                           exchange='default',
                           routing_key='default',
                           arguments={
                               'x': 1,
                               'y': 2
                           })
        print(f"{msg}")


if __name__ == '__main__':
    send_message('Hello World')
