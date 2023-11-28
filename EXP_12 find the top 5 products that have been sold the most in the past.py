import pandas as pd

data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'quantity_sold': [10, 15, 12, 8, 18]
}
sales_data = pd.DataFrame(data)

product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()

top_5_products = product_sales.nlargest(5)

print("Top 5 products sold the most in the past month:")
print(top_5_products)
