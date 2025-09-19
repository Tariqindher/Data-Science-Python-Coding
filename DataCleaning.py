import pandas as pd

# Read CSV file (assuming it's in the same folder)
df = pd.read_csv("data.csv")

# Check basic info
print(df.info())
print(df.head())

# 1. Handle missing values
df["Calories"].fillna(df["Calories"].mean(), inplace=True)   # Replace missing with mean
# 2. Check duplicates
df.drop_duplicates(inplace=True)
# 3. Reset index after cleaning
df.reset_index(drop=True, inplace=True)

print("\nCleaned Data:")
print(df.head())
