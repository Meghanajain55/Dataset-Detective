import pandas as pd

# Load dataset (CSV file)
data = pd.read_csv("dataset.csv")

# Display top 5 rows
print("Top 5 Rows:")
print(data.head())

# Find column with highest value (numeric)
highest_column = data.select_dtypes(include='number').max().idxmax()
print("\nColumn with highest value:", highest_column)

# Count missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Basic insights
print("\nInsights:")
print("1. Dataset contains both numeric and categorical columns.")
print("2. Some columns have missing values.")
print("3. One column has significantly higher values than others.")
print("4. Head function helps preview dataset quickly.")
print("5. Pandas simplifies data exploration.")
