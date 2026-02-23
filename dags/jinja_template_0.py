import pendulum
from pprint import pprint

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG
from airflow.sdk.definitions.decorators import task


@task(task_id = "show_templates")
def show_templates(**kwargs):
    pprint(kwargs)

with DAG(
    dag_id="jinja_template_0",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026,1,1, tz='Asia/Seoul'),
    catchup=True,
    tags=["jinja_template"],
) :
    bash_task_0 = BashOperator(
        task_id="bash_task_0",
        bash_command='echo "Variable> ds : {{ ds }}"',
    )

    # data_interval_start/end , logical_date 은 pendulum.DateTime 객체이기 때문에, Jinja 안에서 .in_timezone() 메서드를 바로 호출할 수 있다.
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        bash_command='echo "Variable> dag : {{ dag }}" && echo "Variable> data_interval_end : {{ data_interval_end.in_timezone(\'Asia/Seoul\') }}"',
    )

    bash_task_2 = BashOperator(
        task_id='bash_task_2',
        env={'START_DATE': '{{ data_interval_start.in_timezone(\'Asia/Seoul\') }}',
             'END_DATE': '{{ data_interval_end.in_timezone(\'Asia/Seoul\') }}'},
        bash_command='echo \'##########\' && '
                     'echo "Start date is $START_DATE " && '
                     'echo "End date is $END_DATE" && '
                     'echo \'##########\''
    )

    bash_task_3 = BashOperator(
        task_id='bash_task_3',
        bash_command='echo \'##########\' && '
                     'echo "Variable > ds : {{ logical_date.in_timezone(\'Asia/Seoul\') | ds }}" && '
                     'echo "Variable > logical_date : {{ logical_date.in_timezone(\'Asia/Seoul\') }}" && '
                     'echo "Variable > data_interval_start : {{ data_interval_start.in_timezone(\'Asia/Seoul\') }}" && '
                     'echo "Variable > data_interval_end : {{ data_interval_end.in_timezone(\'Asia/Seoul\') }}" && '
                     'echo "Variable > dag_run : {{ dag_run }}" && '
                     'echo \'##########\'',
    )

    show_templates = show_templates()

    bash_task_0 >> bash_task_1 >> [ bash_task_2, bash_task_3 ] >> show_templates