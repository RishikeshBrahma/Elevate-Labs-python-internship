

# 1. SETUP AND IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import io

print("--- Step 1: Libraries imported successfully! ---")

# 2. LOADING THE DATA
# In a real scenario, you would use: df = pd.read_csv('your_sales_data.csv')
# For this example, we create data in-memory.
csv_data = """OrderID,Product,Category,Price,UnitsSold,OrderDate,City
101,Laptop,Electronics,1200,5,2025-01-15,New York
102,Mouse,Accessories,25,20,2025-01-17,London
103,Keyboard,Accessories,75,15,2025-01-19,Tokyo
104,Monitor,Electronics,300,10,2025-02-05,New York
105,Laptop,Electronics,1200,3,2025-02-08,Tokyo
106,Webcam,Accessories,50,30,2025-02-12,London
107,Monitor,Electronics,300,8,2025-03-21,New York
108,Mouse,Accessories,25,50,2025-03-25,Tokyo
109,Laptop,Electronics,1200,7,2025-04-02,London
110,Keyboard,Accessories,75,12,2025-04-15,New York
"""

# Read the data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))
print("\n--- Step 2: Data Loaded ---")
print("Original Data Head:")
print(df.head())


# 3. DATA EXPLORATION AND CLEANING
print("\n--- Step 3: Cleaning Data ---")

# Convert 'OrderDate' column to datetime objects for time-series analysis
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create a 'TotalSale' column for analysis
df['TotalSale'] = df['Price'] * df['UnitsSold']

print("\nCleaned DataFrame Head with 'TotalSale' column:")
print(df.head())
print("\nDataFrame Info after cleaning:")
df.info()


# 4. PERFORMING ANALYSIS
print("\n--- Step 4: Analyzing Data ---")

# a) Calculate total sales by product category
category_sales = df.groupby('Category')['TotalSale'].sum().sort_values(ascending=False)
print("\nTotal Sales by Category:")
print(category_sales)

# b) Calculate monthly sales trend
# We set OrderDate as the index to resample data by month
df_resampled = df.set_index('OrderDate')
monthly_sales = df_resampled['TotalSale'].resample('ME').sum()
print("\nTotal Monthly Sales:")
print(monthly_sales)


# 5. DATA VISUALIZATION (CHART)
print("\n--- Step 5: Generating Chart ---")
print("Displaying monthly sales trend chart...")

# 

# Set the style for the plot for better aesthetics
plt.style.use('seaborn-v0_8-whitegrid')

# Create the plot with a specific size
plt.figure(figsize=(10, 6))

# Plot the monthly sales data as a line chart with markers
monthly_sales.plot(kind='line', marker='o', linestyle='-')

# Add titles and labels for clarity
plt.title('Monthly Sales Trend (Jan-Apr 2025)', fontsize=16)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.xticks(rotation=0) # Keep month labels horizontal for readability
plt.grid(True)

# Adjust plot to ensure everything fits without overlapping
plt.tight_layout()

# Display the final chart
plt.show()