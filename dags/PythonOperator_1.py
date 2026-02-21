import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator

from python.sample_PythonOperator_1 import get_job_run_info

with DAG(
    dag_id="PythonOperator_1",
    schedule="1/30 22 * * *",
    start_date=pendulum.datetime(2026, 2, 21, tz="Asia/Seoul"),
    catchup=False,
):
    task_py_1 = PythonOperator(
        task_id="task_py_1",
        python_callable=get_job_run_info,
        # op_kwargs={},
        op_args=["jungmo in op_args"]
    )
    task_bash_1 = BashOperator(
        task_id="task_bash_1",
        bash_command="sleep 5",
    )

    task_bash_2 = BashOperator(
        task_id="task_bash_2",
        bash_command="echo $(date +%Y-%m-%d %H:%M:%S)",
    )

    task_py_2 = PythonOperator(
        task_id="task_py_2",
        python_callable=get_job_run_info,
        op_kwargs={
            "owner":"jungmo in op_kwargs",
        },
        # op_args={},
    )

    task_empty_1 = EmptyOperator(
        task_id="task_empty_1",
    )

    task_empty_2 = EmptyOperator(
        task_id="task_empty_2",
    )

    task_py_1 >> [task_bash_1, task_empty_1] >> task_empty_2 >> task_py_2
    task_bash_2 >> task_py_2
