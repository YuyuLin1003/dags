from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'yuyu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_catchup_backfill_v06',
    default_args=default_args,
    start_date=datetime(2023, 2, 1),
    schedule_interval='@daily',
    catchup=False
)as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command'
    )
