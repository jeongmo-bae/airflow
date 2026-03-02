import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

with DAG(
    dag_id = 'macros_0',
    schedule = '0 0 L * *',
    start_date=pendulum.datetime(2025, 1, 1,tz='Asia/Seoul'),
    catchup = True,
    tags = ['macros']
) :
    bash_task_0 = BashOperator(
        task_id = 'bash_task_0',
        env={
        'START_DATE': '{{ (data_interval_end.in_timezone(\'Asia/Seoul\') + macros.dateutil.relativedelta.relativedelta(days=-1)).strftime("%Y-%m-%d") }}',
        'END_DATE': '{{ data_interval_end.in_timezone(\'Asia/Seoul\').strftime("%Y-%m-%d") }}',
        },
        bash_command = 'echo "####################" &&'
                       'echo "START_DATE : ${START_DATE}" &&'
                       'echo "END_DATE : ${END_DATE}" &&'
                       'echo "####################"',
    )
    # START_DATE : 2주전 월요일 , END_DATE : 2주전 토요일
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={
            'START_DATE': '{{ (data_interval_end.in_timezone(\'Asia/Seoul\') + macros.dateutil.relativedelta.relativedelta(days=-data_interval_end.in_timezone(\'Asia/Seoul\').weekday()+0)).strftime("%Y-%m-%d") }}',
            'END_DATE': '{{ (data_interval_end.in_timezone(\'Asia/Seoul\') + macros.dateutil.relativedelta.relativedelta(days=-data_interval_end.in_timezone(\'Asia/Seoul\').weekday()+5)).strftime("%Y-%m-%d")  }}',
        },
        bash_command='echo "####################" &&'
                     'echo "START_DATE : ${START_DATE}" &&'
                     'echo "END_DATE : ${END_DATE}" &&'
                     'echo "####################"',
    )

    bash_task_0 >> bash_task_1