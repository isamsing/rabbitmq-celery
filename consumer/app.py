from celery import Celery
from config import CeleryConfig
from tasks.add import Add
from tasks.print import Print


celery = Celery(
    'test',
    broker='pyamqp://user:password@localhost:5672/',
    include=["tasks.add"])

celery.register_task(Add())
celery.register_task(Print())
celery.config_from_object(CeleryConfig)

if __name__ == '__main__':
    app.main()