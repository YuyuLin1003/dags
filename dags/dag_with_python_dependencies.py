from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'yuyu',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit learn with version: {sklearn.__version__}")
with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_dependency_v06',
    start_date=datetime(2023, 2, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='scikit',
        python_callable=get_sklearn
    )

    task1