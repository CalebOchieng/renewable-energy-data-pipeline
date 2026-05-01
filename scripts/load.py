import sqlite3


def load_data(df):
    conn = sqlite3.connect("energy.db")

    # Fact table
    fact_table = df[[
        "project_id", "date", "energy_generated_kwh",
        "revenue", "cost", "profit"
    ]]
    fact_table.to_sql("fact_energy", conn, if_exists="replace", index=False)

    # Project dimension
    dim_project = df[[
        "project_id", "project_name", "region", "installation_date"
    ]].drop_duplicates()
    dim_project.to_sql("dim_project", conn, if_exists="replace", index=False)

    # Customer dimension
    dim_customer = df[[
        "project_id", "number_of_customers"
    ]].drop_duplicates()
    dim_customer.to_sql("dim_customer", conn, if_exists="replace", index=False)

    conn.close()
