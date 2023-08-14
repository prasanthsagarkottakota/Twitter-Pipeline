from datetime import datetime, timedelta
from airflow import DAG
from airflow.operator.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl

default_args:{
	'owner' : 'Prasanth Sagar',
	'depends_on_past' : False,
	'start_date' : datetime(2023,7,29),
	'email' : ['kpsagar1999@gmail.com'],
	'email_on_failure' : True,
	'email_on_retry' : False,
	'retries' : 2,
	'retries_dealy': timedelta(minutes = 1)
}

dag = DAG('twitter_dag_project',default_args = default_args, description= 'using airflow, ec2, s3',schedule_interval= timedelta(days = 1),)

run_etl = PythonOperator(task_id = "execute run_twitter_etl", python_callable =  run_twitter_etl, dag = dag,)

run_etl