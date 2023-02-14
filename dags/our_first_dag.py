from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    dag_id='our_first_dag_v4',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2023, 2, 14),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(task_id='first_task',
                         bash_command="echo hello world, this is the first task!")
    task2 = BashOperator(task_id='second_task',
                         bash_command="echo hello, this is the second task!,it will run after task1")
    task3 = BashOperator(task_id='third_task',
                         bash_command="echo hello, this is the third task!it will run after task 1 and as the same time as task 1")
    #  task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    #  task dependency method 2
    # task1 >> task2
    # task1 >> task3

    #  task dependency method 3
    task1 