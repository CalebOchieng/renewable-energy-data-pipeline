import sqlite3
import pandas as pd

conn = sqlite3.connect("energy.db")

queries = {
    "Energy by Region": """
        SELECT p.region, SUM(f.energy_generated_kwh) AS total_energy
        FROM fact_energy f
        JOIN dim_project p ON f.project_id = p.project_id
        GROUP BY p.region;
    """,

    "Profit by Project": """
        SELECT p.project_name, SUM(f.profit) AS total_profit
        FROM fact_energy f
        JOIN dim_project p ON f.project_id = p.project_id
        GROUP BY p.project_name;
    """,

    "Revenue per Customer": """
        SELECT p.project_name, SUM(f.revenue) / c.number_of_customers AS revenue_per_customer
        FROM fact_energy f
        JOIN dim_project p ON f.project_id = p.project_id
        JOIN dim_customer c ON f.project_id = c.project_id
        GROUP BY p.project_name, c.number_of_customers;
    """,

    "Efficiency (energy per Customer)": """
        SELECT p.project_name, SUM(f.energy_generated_kwh) / c.number_of_customers AS energy_per_customer
        FROM fact_energy f
        JOIN dim_project p ON f.project_id = p.project_id
        JOIN dim_customer c ON f.project_id = c.project_id
        GROUP BY p.project_name;
    """,

    "Monthly revenue trend": """
        SELECT date, SUM(revenue) AS total_revenue
        FROM fact_energy
        GROUP BY date
        ORDER BY date;
    """
}

for name, query in queries.items():
    print(f"\n--- {name} ---")
    df = pd.read_sql(query, conn)
    print(df)

    df.to_csv(
        f"data/processed/{name.lower().replace(' ', '_')}.csv", index=False)

    df1 = pd.read_sql("SELECT * FROM fact_energy", conn)
    df2 = pd.read_sql("SELECT * FROM dim_project", conn)
    df3 = pd.read_sql("SELECT * FROM dim_customer", conn)

    df1.to_csv("fact_energy.csv", index=False)
    df2.to_csv("dim_project.csv", index=False)
    df3.to_csv("dim_customer.csv", index=False)

conn.close()
