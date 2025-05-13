from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Importando nosso operador personalizado
# É importante que o plugin esteja configurado corretamente para que esta importação funcione
try:
    from plugins.operators.hello_operator import HelloOperator
except ImportError:
    from airflow.operators.bash import BashOperator as HelloOperator
    print("Erro ao importar HelloOperator! Usando BashOperator como fallback")

# Argumentos padrão para a DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definição da DAG
dag = DAG(
    'plugin_exemplo',
    default_args=default_args,
    description='Uma DAG de exemplo usando um plugin personalizado',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['exemplo', 'plugin'],
)

# Tarefa usando nosso operador personalizado
hello_task = HelloOperator(
    task_id='diga_ola',
    name='Desenvolvedor',
    dag=dag,
)

# Função Python para ser executada em sequência
def processar_mensagem(**kwargs):
    ti = kwargs['ti']
    try:
        mensagem = ti.xcom_pull(task_ids='diga_ola')
        print(f"Mensagem recebida: {mensagem}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        mensagem = "Mensagem padrão"
    return "Processamento concluído"

# Tarefa que executa uma função Python
processar_task = PythonOperator(
    task_id='processar_mensagem',
    python_callable=processar_mensagem,
    dag=dag,
)

# Definição da ordem de execução das tarefas
hello_task >> processar_task 