# Modern Data Engineering Pipeline for E-commerce Orders

**Prepared by:** Mina Gerges Attia

This project demonstrates an end-to-end modern data engineering pipeline for e-commerce orders data using **DuckDB**, **dbt**, **Airflow**, and **Docker**.

## Project Overview
The pipeline processes raw CSV files for:
- Orders
- Payments
- Customers

It loads them into DuckDB, transforms them with dbt, validates them with tests, and orchestrates the workflow through Airflow.

## Tech Stack
- DuckDB
- dbt
- Apache Airflow
- Docker

## Project Structure
```text
dbt_withDuckDB/
├── dags/
├── data/
├── dbt_project/
├── scripts/
├── Dockerfile
├── docker-compose.yml
└── README.md