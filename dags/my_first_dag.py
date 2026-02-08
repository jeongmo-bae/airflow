from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator

def print_hello():
    print("Hello Airflow!")

with DAG(
    dag_id="sample_dag",
    description="A simple DAG",
    schedule="0 0 * * *",
    start_date=datetime(2026, 2, 9),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="print_hello_task",
        python_callable=print_hello,
    )

    task2 = EmptyOperator(
        task_id="dummy_task",
    )

task1 >> task2