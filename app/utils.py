import os
import pandas as pd

def load_all_data(data_path):
    """Load all country data from Cleaned-data"""
    return {
        "benin": pd.read_csv(os.path.join(data_path, "benin_clean.csv")),
        "sierra_leone": pd.read_csv(os.path.join(data_path, "sierra_leone_clean.csv")),
        "togo": pd.read_csv(os.path.join(data_path, "togo_clean.csv"))
    }

def compare_countries(data):
    """Generate comparison statistics"""
    return pd.DataFrame({
        country: df['GHI'].describe()
        for country, df in data.items()
    }).T