import pandas as pd

# Load the data from a CSV file into a DataFrame
sales_df = pd.read_csv('sales_data.csv')

# Calculate the Total_Price column (price * quantity)
sales_df['Total_Price'] = sales_df['Price'] * sales_df['Quantity']

# What was the total revenue from all sales?
total_revenue = sales_df['Total_Price'].sum()

# What was the most expensive single item sold?
most_expensive_item_price = sales_df['Price'].max()
# Find the row with the price
most_expensive_item_details = sales_df[sales_df['Price'] == most_expensive_item_price]

# How many laptops were sold?
laptops_sold = sales_df[sales_df['Product'] == 'Laptop']['Quantity'].sum()

# Print all answers
print('--- Sales Analysis Report ---')
print(f'Total Revenue: ${total_revenue:.2f}')
print(f'Most expensive item details\n{most_expensive_item_details}')
print(f'Total Laptops Sold: {laptops_sold}')