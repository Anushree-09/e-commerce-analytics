from data.scripts.extract import extract_data
from data.scripts.transform import transform_data
from data.scripts.load import load_data

def run_pipeline():
    orders, customers, items, payments = extract_data()
    transformed_df = transform_data(orders, customers, items, payments)
    load_data(transformed_df)

if __name__ == "__main__":
    run_pipeline()