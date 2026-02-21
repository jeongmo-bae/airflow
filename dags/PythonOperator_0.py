import random

import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG


def hello_python_operator(**kwargs):
    print("========== START ==========")
    print('start_date : {}'.format(kwargs.get("start_date")))
    print('contents : {}'.format(kwargs.get("contents")))
    print("========== END ==========")

    return random.randint(0,10)

with DAG(
    dag_id="PythonOperator_0",
    schedule="1 * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # default_args={"owner": "airflow"},
):
    task_py_1 = PythonOperator(
        task_id="task_py_1",
        python_callable=hello_python_operator,
        op_kwargs={
            "start_date": pendulum.now(tz="Asia/Seoul"),
            "contents" : "task1 : hello PythonOperator",
        },
    )

    task_py_2 = PythonOperator(
        task_id="task_py_2",
        python_callable=hello_python_operator,
        op_kwargs={
            "start_date": pendulum.now(tz="Asia/Seoul"),
            "contents" : "task2 : if task1 success, do",
        }
    )

    task_py_1 >> task_py_2