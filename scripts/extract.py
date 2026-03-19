import pandas as pd

def extract_data():
    orders = pd.read_csv("data/orders.csv")
    customers = pd.read_csv("data/customers.csv")
    items = pd.read_csv("data/order_items.csv")
    payments = pd.read_csv("data/payments.csv")

    return orders, customers, items, payments