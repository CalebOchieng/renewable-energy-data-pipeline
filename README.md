📊 Renewable Energy Data Pipeline & Analytics Dashboard

📌 Overview

This project demonstrates an end-to-end data workflow, from raw data ingestion to business insights. It focuses on renewable energy performance analysis across multiple regions and projects.

⚙️ Tech Stack
Python (Pandas) – Data extraction and transformation
SQLite – Data storage and modeling
SQL – Data querying and aggregation
Power BI – Data visualization and dashboarding


🧱 Data Architecture

The project follows a modular ETL pipeline:

Extract – Load raw CSV datasets
Transform – Clean, merge, and engineer features
Load – Store processed data in a structured database


🗂️ Data Model

Implemented a star schema:

Fact Table: fact_energy
Dimension Tables:
dim_project
dim_customer

This structure enables efficient querying and scalable analytics.

📊 Dashboard Features
![Dashboard](dashboard.png)
Energy generation by region
Revenue and profit analysis
Cost vs revenue efficiency analysis
KPI tracking (Revenue, Energy, Efficiency)
Interactive filters (region, project, date)
Dynamic highlighting of top-performing regions


🔍 Key Insights
Mombasa is the top-performing region in both energy output and revenue
Solar Grid E is the most profitable project
Revenue shows steady growth over time
Variations in cost efficiency highlight opportunities for optimization
