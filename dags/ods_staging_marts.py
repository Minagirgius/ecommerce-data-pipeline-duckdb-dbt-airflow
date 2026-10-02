from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

PROJECT_DIR = "/opt/airflow/dbt_project"
SCRIPT_PATH = "/opt/airflow/scripts/load_to_ods.py"

with DAG(
    dag_id="ods_staging_marts",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["duckdb", "dbt"],
) as dag:

    load_to_ods = BashOperator(
        task_id="load_to_ods",
        bash_command=f"python {SCRIPT_PATH}"
    )

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command=f"cd {PROJECT_DIR} && dbt run --profiles-dir . --select staging"
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command=f"cd {PROJECT_DIR} && dbt run --profiles-dir . --select marts"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {PROJECT_DIR} && dbt test --profiles-dir ."
    )

    load_to_ods >> dbt_staging >> dbt_marts >> dbt_test