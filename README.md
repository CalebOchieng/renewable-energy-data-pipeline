# 📊 Renewable Energy Data Pipeline & Analytics Dashboard

## 📌 Overview
This project demonstrates an end-to-end data workflow for analyzing renewable energy performance across multiple regions and projects. It integrates data engineering, data modeling, and business intelligence to transform raw data into actionable insights.

---

## 🎯 Objectives
- Build a modular ETL pipeline to process multi-source data  
- Design a scalable data model for analytics  
- Generate business insights using SQL  
- Develop an interactive dashboard for decision-making  

---

## ⚙️ Tech Stack
- **Python (Pandas)** – Data extraction, cleaning, and transformation  
- **SQLite** – Data storage and relational modeling  
- **SQL** – Querying and aggregations  
- **Power BI** – Data visualization and dashboard development  

---

## 🧱 Data Pipeline Architecture

The project follows a structured ETL approach:

### 1. Extract
- Load raw datasets (projects, energy production, customers, financials)

### 2. Transform
- Clean and standardize data  
- Merge datasets into a unified structure  
- Create derived metrics:
  - Revenue per customer  
  - Profit  
- Apply validation checks for data quality  

### 3. Load
- Store processed data into a relational database  
- Organize data into analytics-ready tables  

---

## 🗂️ Data Model

A **star schema** was implemented to support efficient querying:

### ⭐ Fact Table
- `fact_energy`  
  - energy_generated_kwh  
  - revenue  
  - cost  
  - profit  
  - date  

### 📦 Dimension Tables
- `dim_project` (project details, region)  
- `dim_customer` (customer counts)  

---

## 📊 Dashboard Features

The Power BI dashboard provides:

- **KPI Tracking**
  - Total Revenue (KES)  
  - Total Energy Generated (kWh)  
  - Revenue per Customer  
  - Energy per Customer  

- **Performance Analysis**
  - Energy generation by region  
  - Profit by project  
  - Monthly revenue trends  

- **Efficiency Insights**
  - Cost vs revenue analysis  
  - Energy per customer metrics  

- **Interactivity**
  - Filters by region, project, and date  
  - Dynamic highlighting of top-performing regions using DAX  

---

## 🔍 Key Insights

- Mombasa is the top-performing region in both energy generation and revenue  
- Solar Grid E delivers the highest profitability  
- Revenue shows consistent growth over time  
- Cost efficiency varies across projects, indicating optimization opportunities  

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/renewable-energy-data-pipeline.git
cd renewable-energy-data-pipeline
```

### 2. Run the ETL pipeline
```bash
python main.py
```

### 3. Query the data (optional)
```bash
python query.py
```

### 4. Open dashboard
- Import exported CSV files into Power BI  
- Or connect to processed data outputs  

---

## 📁 Project Structure

```bash
energy-data-project/
│── data/
│   ├── raw/
│   ├── processed/
│── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│── main.py
│── query.py
│── README.md
```

---

## 📈 Future Improvements

- Integrate cloud-based pipelines (Azure / AWS)  
- Implement dbt for transformation workflows  
- Automate pipeline scheduling  
- Connect to live data sources (APIs)  
- Deploy dashboard for real-time access  

---

## 💡 Key Learnings

- Building modular ETL pipelines improves scalability and maintainability  
- Star schema design enhances query performance  
- Combining SQL and BI tools enables effective decision support  
- Data storytelling is critical for communicating insights  

---

## 📸 Dashboard Preview
![Dashboard](dashboard/dashboard.png)

---

## 📬 Contact
If you’d like to discuss this project or opportunities in data engineering/analytics, feel free to connect.
