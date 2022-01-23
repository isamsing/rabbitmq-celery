from kombu import Queue, Exchange


class CeleryConfig:

    CELERY_QUEUES = ([
        Queue('adder', Exchange('default'), routing_key='tasks.add'),
        Queue('print', Exchange('default'), routing_key='tasks.print')
    ])
