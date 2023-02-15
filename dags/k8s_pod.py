from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

from datetime import datetime
from airflow import DAG
k = KubernetesPodOperator(
    name="hello-dry-run",
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    labels={"foo": "bar"},
    task_id="dry_run_demo",
    do_xcom_push=True,
)

with DAG(dag_id="dynamic_task_pod_20", start_date=datetime.utcnow()) as dag:
    k.dry_run()