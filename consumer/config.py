from kombu import Queue, Exchange


class CeleryConfig:

    CELERY_QUEUES = ([
        Queue('adder', Exchange('adder'), routing_key='tasks.add'),
        Queue('print', Exchange('print'), routing_key='tasks.print')
    ])
