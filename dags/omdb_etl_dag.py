from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from omdb import extract, update_airflow_values
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 10),
    'email': ['sadiquetimileyin@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}


def initialize(**kwargs):
    ti = kwargs['ti']
    start = 41
    end = 50
    ti.xcom_push(key='start', value=start)
    ti.xcom_push(key='end', value=end)


with DAG(
    'update_movie_data_dag',
    default_args=default_args,
    description='A simple DAG to update movie data daily',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    initialize = PythonOperator(
        task_id='initialize',
        python_callable=initialize,
        provide_context=True
    )

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True
    )

    update_values = PythonOperator(
        task_id='update_values',
        python_callable=update_airflow_values,
        provide_context=True
    )

    initialize >> extract_task >> update_values

