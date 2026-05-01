from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data


def run_pipeline():
    print("Starting ETL pipeline...")

    projects, energy, customers, financials = extract_data()
    print("Data extracted successfully")

    transformed_data = transform_data(projects, energy, customers, financials)
    print("Data transformed")

    load_data(transformed_data)
    print("Data loaded into database")


if __name__ == "__main__":
    run_pipeline()
