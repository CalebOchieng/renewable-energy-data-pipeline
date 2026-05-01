import pandas as pd


def extract_data():
    projects = pd.read_csv("data/raw/projects.csv")
    energy = pd.read_csv("data/raw/energy_production.csv")
    customers = pd.read_csv("data/raw/customers.csv")
    financials = pd.read_csv("data/raw/financials.csv")

    return projects, energy, customers, financials
