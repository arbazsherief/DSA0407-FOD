import pandas as pd

data = {
    'customer_id': [1, 1, 2, 3, 3],
    'order_date': ['2023-01-01', '2023-01-05', '2023-01-02', '2023-02-01', '2023-02-15'],
    'product_name': ['A', 'B', 'A', 'C', 'B'],
    'order_quantity': [3, 2, 1, 4, 2]
}
order_data = pd.DataFrame(data)

try:
    orders_per_customer = order_data.groupby('customer_id')['order_date'].count()
    print("Total number of orders made by each customer:")
    print(orders_per_customer)
except KeyError:
    print("Error: 'customer_id' or 'order_date' column not found.")

try:
    average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
    print("\nAverage order quantity for each product:")
    print(average_order_quantity_per_product)
except KeyError:
    print("Error: 'product_name' or 'order_quantity' column not found.")

try:
    order_data['order_date'] = pd.to_datetime(order_data['order_date'])
    earliest_order_date = order_data['order_date'].min()
    latest_order_date = order_data['order_date'].max()
    print(f"\nEarliest order date: {earliest_order_date}")
    print(f"Latest order date: {latest_order_date}")
except KeyError:
    print("Error: 'order_date' column not found.")
