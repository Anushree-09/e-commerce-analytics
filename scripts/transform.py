import pandas as pd
def transform_data(orders, customers, items, payments):

    # Merge datasets
    df = orders.merge(customers, on="customer_id")
    df = df.merge(items, on="order_id")
    df = df.merge(payments, on="order_id")

    # Convert dates
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    # Create new columns
    df['total_amount'] = df['price'] + df['freight_value']
    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

    return df