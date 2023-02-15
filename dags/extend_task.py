from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.decorators import task

with DAG(dag_id="example_dynamic_task_mapping_03", start_date=datetime(2023, 2, 15)) as dag:

    @task
    def add_one(x: int):
        return x + 1

    @task
    def sum_it(values):
        total = sum(values)
        print(f"Total was {total}")
        return total

    added_values = add_one.expand(x=range(1,10))
    sum_it(added_values)