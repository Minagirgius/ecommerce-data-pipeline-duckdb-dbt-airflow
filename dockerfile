FROM apache/airflow:3.3.2

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

USER airflow
RUN pip install --no-cache-dir \
    dbt-core \
    dbt-duckdb \
    duckdb \
    pandas