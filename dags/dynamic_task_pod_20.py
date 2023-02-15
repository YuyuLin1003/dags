from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.decorators import task

def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    lst.pop(0)
    return(lst)
with DAG(dag_id="dynamic_task_pod_20", start_date=datetime.utcnow()) as dag:

    @task
    def add_one(x: int):
        return 1

    @task
    def sum_it(values):
        total = sum(values)
        print(f"Total was {total}")
        return total

    mylist=createList(20)
    added_values = add_one.expand(x=mylist)
    sum_it(added_values)