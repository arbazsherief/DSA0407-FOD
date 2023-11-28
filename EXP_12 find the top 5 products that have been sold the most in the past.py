import pandas as pd

data = {
    'product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I'],
    'quantity': [5, 3, 8, 6, 7, 2, 1, 9, 4]
}
df = pd.DataFrame(data)

product_sales = df.groupby('product')['quantity'].sum()


sorted_product_sales = product_sales.sort_values(ascending=False)

top_5_products = sorted_product_sales.head(5)

print(top_5_products)
