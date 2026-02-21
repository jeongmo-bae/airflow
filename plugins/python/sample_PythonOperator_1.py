import logging

logger = logging.getLogger(__name__)

def get_job_run_info(owner: str, **context):
    logger.info("========== START ==========")
    logger.info(f"owner: {owner}")
    logger.info("===========================")
    logger.info(f"dag_run: {context.get("dag_run")}" )
    logger.info(f"task_instance: {context.get("task_instance")}")
    logger.info(f"run_id: {context.get("run_id")}")
    logger.info("========== END ==========")