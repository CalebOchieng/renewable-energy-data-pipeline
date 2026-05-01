import pandas as pd


def transform_data(projects, energy, customers, financials):
    # Standardize column names
    for df in [projects, energy, customers, financials]:
        df.columns = df.columns.str.lower()

    # Merge datasets
    df = energy.merge(projects, on="project_id")
    df = df.merge(customers, on="project_id")
    df = df.merge(financials, on="project_id")

    # Convert dates
    df["date"] = pd.to_datetime(df["date"])

    # Create metrics
    df["revenue_per_customer"] = df["revenue"] / df["number_of_customers"]
    df["profit"] = df["revenue"] - df["cost"]

    # Remove duplicates
    df = df.drop_duplicates()

    # ✅ DATA VALIDATION (ADD HERE)
    assert df["revenue"].min() >= 0, "Revenue contains negative values"
    assert df["number_of_customers"].min() > 0, "Customers must be > 0"
    assert df["energy_generated_kwh"].min() >= 0, "Energy cannot be negative"
    assert df.isnull().sum().sum() == 0, "Dataset contains null values"

    return df
