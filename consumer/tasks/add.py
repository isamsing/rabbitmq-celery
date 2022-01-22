from celery import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

class Add(Task):
    name = "tasks.add"

    def run(self, x: int, y: int) -> int:
        print('Adding {0} + {1}'.format(x, y))
        return x + y
