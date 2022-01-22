from celery import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class Print(Task):
    name = "tasks.print"

    def run(self, msg: str) -> int:
        logger.info(msg)
