from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Definição da DAG
dag = DAG(
    'teste_simples',
    description='Uma DAG muito simples para teste',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Tarefa simples
t1 = BashOperator(
    task_id='echo_hello',
    bash_command='echo "Olá do Airflow!"',
    dag=dag,
) 