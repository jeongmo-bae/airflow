import pendulum
# import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import (
    DAG,
    # Param,
)
# from airflow.sdk.definitions.param import ParamsDict

with DAG(
    dag_id="BashOperator_1",
    schedule="5/30 * * * *",   # 분 시 일 월 요일
    start_date=pendulum.datetime(2026, 2, 21, tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags={"example", "example2"},
    # params={"example_key": "example_value"}, # params=ParamsDict({"example_key": Param("example_value", type="string")})
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="cd /opt/airflow/plugins/shell; ./script_BashOperator_1.sh ThisIsParam1=task1 ThisIsParam2=$(date +%Y%m%d)",
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="sleep 5",
    )

    task3 = BashOperator(
        task_id="task3",
        bash_command="echo 'sleep 30 ended'",
    )

    task4 = BashOperator(
        task_id="task4",
        bash_command="cd /opt/airflow/plugins/shell; ./script_BashOperator_1.sh ThisIsParam1=task4 ThisIsParam2=$(date +%Y%m%d)",
    )

    task5 = BashOperator(
        task_id="task5",
        bash_command="echo 'All tasks completed'",
    )

    task1 >> task2 >> [task3,task4]  >> task5