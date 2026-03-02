import zoneinfo

import pendulum
from airflow.providers.standard.operators.bash import BashOperator

from airflow.sdk import DAG
from airflow.sdk.definitions.decorators import task
from dateutil.relativedelta import relativedelta

from python.common.log_utils import timer
from python.common.logger import MyLogger

logger = MyLogger(__name__)

@task(
    task_id='task_debugging_start_date',
    templates_dict={
        'start_date' : '{{ data_interval_start.in_timezone("Asia/Seoul") + macros.dateutil.relativedelta.relativedelta(months=-1) }}',
        'end_date' : '{{ data_interval_end.in_timezone("Asia/Seoul") + macros.dateutil.relativedelta.relativedelta(months = -1 ,days = +1) }}',
    }
)
@timer
def debugging_res(res,**kwargs):
    templates_dict=kwargs.get('templates_dict') or {}
    if templates_dict:
        logger.info(f"########## templates_dict : {templates_dict} ##########")
        logger.info(f'start_date : {templates_dict.get("start_date")}')
        logger.info(res)
        logger.info(f'end_date : {templates_dict.get("end_date")}')
    else:
        logger.info("########## templates_dict : None ##########")
        logger.info(f'start_date : {kwargs.get("dag_run").logical_date.astimezone(zoneinfo.ZoneInfo("Asia/Seoul")) + relativedelta(months = -1)}')
        logger.info(res)
        logger.info(f'end_date : {kwargs.get("dag_run").logical_date.astimezone(zoneinfo.ZoneInfo("Asia/Seoul")) + relativedelta(months = -1, days = +1)}')


with DAG(
    dag_id='macros_1',
    default_args={},
    schedule="0 0 L * *",
    start_date=pendulum.datetime(2026, 2, 25,tz='Asia/Seoul'),
    catchup = True,
    tags=['macros'],
) :
    task_bash = BashOperator(
        task_id='task_bash',
        env={'START_DATE': '{{ data_interval_start.in_timezone(\'Asia/Seoul\') + macros.dateutil.relativedelta.relativedelta(months = -1) }}',
             'END_DATE': '{{ data_interval_end.in_timezone(\'Asia/Seoul\') }}'},
        bash_command='echo "START_DATE=${START_DATE}" && '
                     'echo "END_DATE=${END_DATE}" ',
    )

    task_debugging_start_date = debugging_res('macros in python operator')

    task_bash >> task_debugging_start_date