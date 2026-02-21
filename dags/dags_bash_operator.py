import pendulum
# import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import (
    DAG,
    # Param,
)
# from airflow.sdk.definitions.param import ParamsDict

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",   # 분 시 일 월 요일
    start_date=pendulum.datetime(2026, 2, 21, tz="Asia/Seoul"),
    catchup=False,   # start_date 부터 현재시각 사이를 모두 수행 시킬거냐 - 순서대로 X = 멱등적인지에 따라 문제가 될 수도
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags={"example", "example2"},
    # params={"example_key": "example_value"}, # params=ParamsDict({"example_key": Param("example_value", type="string")})
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo $(whoami)",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME; echo good",
    )

    bash_t3 = BashOperator(
        task_id="bash_t3",
        bash_command="echo $HOSTNAME; echo good",
    )

    bash_t4 = BashOperator(
        task_id="bash_t4",
        bash_command="echo $HOSTNAME; echo good",
    )

    bash_t1 >> bash_t2 >> bash_t3 >> bash_t4