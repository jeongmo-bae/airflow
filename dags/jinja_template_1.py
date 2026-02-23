import logging

from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
import pendulum
from airflow.sdk.definitions.decorators import task

from python.common.log_utils import timer

logger = logging.getLogger(__name__)
@task(task_id='test_jinja_with_task_decorator')
@timer
def test_jinja_with_task_decorator(**kwargs):
    logger.info('--------------------')
    logger.info(f"task_instance : {kwargs.get('ti')}")
    logger.info(f"none : {kwargs.get('aaaaaaaaaaaa')}")
    logger.info(f"ds : {kwargs.get('logical_date').in_timezone('Asia/Seoul').strftime('%Y-%m-%d')}")
    logger.info(f"ts : {kwargs.get('logical_date').in_timezone('Asia/Seoul')}")
    logger.info(f"data_interval_start : {kwargs.get('data_interval_start')}")
    logger.info(f"data_interval_end : {kwargs.get('data_interval_end')}")
    logger.info('--------------------')
    logger.info(f"{kwargs}")
    logger.info('--------------------')

@timer
def test_jinja_with_python_operator(custom_start_date,custom_end_date,**kwargs):
    logger.info('--------------------')
    logger.info(f"ds : {kwargs.get('logical_date').in_timezone('Asia/Seoul').strftime('%Y-%m-%d')}")
    logger.info(f"ts : {kwargs.get('logical_date').in_timezone('Asia/Seoul')}")
    logger.info(f"start_date : {custom_start_date}")
    logger.info(f"end_date : {custom_end_date}")
    logger.info('--------------------')
    logger.info(f"{kwargs}")
    logger.info('--------------------')


with DAG(
    dag_id='jinja_template_1',
    schedule='1 1 * * *',
    start_date=pendulum.datetime(2026, 2, 1,tz='Asia/Seoul'),
    catchup=True,
    tags=['jinja_template'],
) :

    test_jinja_with_python_operator = PythonOperator(
        task_id='test_jinja_with_python_operator',
        python_callable=test_jinja_with_python_operator,
        op_kwargs={
            'custom_start_date': '{{ logical_date.in_timezone(\'Asia/Seoul\') | ds }}',
            'custom_end_date': '{{ logical_date.in_timezone(\'Asia/Seoul\') | ds }}'
        }
    )
    test_jinja_with_task_decorator = test_jinja_with_task_decorator()

    empty_task = EmptyOperator(
        task_id='empty_task',
    )

    empty_task >> [test_jinja_with_task_decorator , test_jinja_with_python_operator]