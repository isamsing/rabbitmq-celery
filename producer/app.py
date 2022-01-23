import time
import random

from celery import Celery

celery = Celery(
    'producer',
    broker='pyamqp://user:password@rabbitmq:5672',
)

numTasks = 100
tasks = []

for i in range(numTasks):
    time.sleep(2 * random.random())  # Random delay
    tasks.append(
        celery.send_task(name='tasks.add', exchange='default', queue='adder', kwargs={
            'x': i,
            'y': 6
        })
    )
    print('Sent task:', i)

if __name__ == '__main__':
    pass
