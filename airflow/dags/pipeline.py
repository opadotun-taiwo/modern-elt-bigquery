from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import os
import sys

# Paths inside the container
PYTHON_SCRIPT_PATH = "/opt/airflow/api_request/insert_records.py"
DBT_PROJECT_DIR = "/opt/dbt/weather_dbt"
DBT_PROFILES_DIR = "/opt/dbt/profiles"

# Safe Python ETL wrapper
def run_python_etl_safe():
    try:
        # Add the script folder to sys.path
        script_dir = os.path.dirname(PYTHON_SCRIPT_PATH)
        sys.path.insert(0, script_dir)

        # Import your ETL script
        import insert_records

        # Run main
        insert_records.main()
    except ModuleNotFoundError:
        print(f"Module 'insert_records' not found at {PYTHON_SCRIPT_PATH}.")
        # For now, just log instead of failing
    except Exception as e:
        print(f"Error running Python ETL: {e}")

# Default DAG arguments
default_args = {
    "owner": "taiwo",
    "start_date": datetime(2026, 2, 1),
    "retries": 1,
}

# DAG definition
with DAG(
    dag_id="python_dbt_bigquery",
    default_args=default_args,
    schedule=None,  # manual trigger
    catchup=False,
    tags=["etl", "dbt", "bigquery"]
) as dag:

    # Task 1: Python ETL
    etl_task = PythonOperator(
        task_id="run_python_etl",
        python_callable=run_python_etl_safe
    )

    # Task 2: dbt models
    dbt_task = BashOperator(
        task_id="run_dbt_models",
        bash_command=f"""
            cd {DBT_PROJECT_DIR} && \
            dbt run \
            --project-dir {DBT_PROJECT_DIR} \
            --profiles-dir {DBT_PROFILES_DIR}
        """
    )

    etl_task >> dbt_task
