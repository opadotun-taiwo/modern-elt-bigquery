##End-to-End ELT Analytics Pipeline
![Weather Dashboard](images/weather_dashboard.png)

This project demonstrates a modern ELT analytics architecture, covering the full lifecycle of data — from ingestion to analytics-ready models and exploration.

The goal is to show not just dashboarding, but how to design, build, and operate a reliable analytics system using production-style tooling and workflows.

Architecture Overview

#Flow:

External API → Python Ingestion → BigQuery (raw) 
→ dbt (staging → marts) → Apache Superset


Key Principles:

ELT (transform inside the warehouse)

Clear data layer separation

Reproducible, containerized environments

Version-controlled analytics logic

Tech Stack

Python – API data ingestion

BigQuery – Cloud data warehouse

dbt – Transformations (staging & marts)

Apache Superset – Data exploration & analytics

Docker – Environment consistency

Git – Version control

Data Modeling Approach

Raw layer: API data loaded directly into BigQuery with minimal transformation

Staging models (stg_): Cleaned, typed, and standardized data

Mart models: Analytics-ready tables designed for reporting and exploration

This structure enables reuse, testing, and downstream stability.

Running the Project
Prerequisites

Docker & Docker Compose

GCP project with BigQuery enabled

dbt profile configured for BigQuery

Start Services
docker compose up --build


This spins up:

dbt environment

Apache Superset with BigQuery support

Key Challenges & How They Were Solved
1. dbt Adapter Version Mismatch (Local vs Docker)

Problem:
Different dbt adapter versions between local and containerized environments caused runtime errors and inconsistent behavior.

Solution:

Standardized Python to 3.10

Aligned dbt-core and BigQuery adapter versions across environments

Locked dependencies in Docker for consistency

Outcome:
Reproducible builds and predictable dbt execution across environments.

2. Superset Lacking Native BigQuery Support

Problem:
Default Superset image did not include the BigQuery connector.

Solution:

Built a custom Superset Docker image

Installed required BigQuery dependencies and adapters

Ensured compatibility with existing Superset setup

Outcome:
Superset connected seamlessly to BigQuery, enabling exploration of analytics models.

3. Environment Reproducibility

Problem:
Local setup drift made onboarding and debugging harder.

Solution:

Containerized all services using Docker

Version-controlled configuration and models with Git

Outcome:
Anyone can clone the repo and run the full stack with minimal setup.
![Weather Dashboard](images/weather_dashboard.png)
