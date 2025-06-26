import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price_usd': [1200, 25, 75, 300],
    'in_stock': [True, True, False, True]
}
df = pd.DataFrame(data)
print('--- Our Product DataFrame ---')
print(df)

print('\n--- First 2 rows ---')
print(df.head(2))

print('\n--- Basic Info ---')
print(df.info())

# Select a single column (returns a Series)
prices = df['price_usd']
print(f"\n--- Prices Series ---\n{prices}")

# Select multiple columns (returns a DataFrame)
products_and_prices = df[['product_name', 'price_usd']]
print(f'\n--- Products and Prices DF ---\n{products_and_prices}')


# Find all products that cost more than $100
expensive_products = df[df['price_usd'] > 100]
print(f'\n--- Expensive Products ---\n{expensive_products}')

# Find all products that are out of stock
out_of_stock = df[df['in_stock'] == False]
print(f'\n--- Out of Stock ---\n{out_of_stock}')

# Add a new column based on existing data
df['price_lkr'] = df['price_usd'] * 300
print(f'\n--- DataFrame with LKR Prices ---\n{df}')
