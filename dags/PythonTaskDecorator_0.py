import pendulum

from airflow.sdk import DAG
from airflow.sdk.definitions.decorators import task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

from python.common.timer import timer
from python.sample_PythonOperator_1 import get_job_run_info

@task(task_id="task_get_job_run_info")
@timer
def task_get_job_run_info(owner,**context):
    return get_job_run_info(owner,**context)


with DAG(
    dag_id="PythonTaskDecorator_0",
    schedule="0/15 * * * *",
    start_date=pendulum.datetime(2026, 2, 21,tz="Asia/Seoul"),
    catchup=False,
    tags=["TaskDecorator"],
) :
    task_get_job_run_info = task_get_job_run_info(owner="jungmo")
    task_bash_operator_echo = BashOperator(
        task_id="task_bash_operator_echo",
        bash_command="echo 'PIPELINE IS ENDED'",
    )
    task_bash_operator_sleep = BashOperator(
        task_id="task_bash_operator_sleep",
        bash_command="sleep 5",
    )

    task_empty_operator = EmptyOperator(
        task_id="task_empty_operator",
    )

    task_empty_operator >> task_bash_operator_echo
    task_bash_operator_sleep >> task_get_job_run_info >> task_bash_operator_echo



