"""
DAG básica para testar se o Airflow consegue detectar DAGs
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'basic',
    description='Uma DAG básica',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag
)

t1 >> t2 