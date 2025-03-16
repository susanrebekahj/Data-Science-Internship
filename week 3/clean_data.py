import pandas as pd

# Load dataset (replace 'file.csv' with your actual file name)
df = pd.read_csv('file.csv')

# Check first few rows
print("Original Data:")
print(df.head())

# Remove missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)


# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Save cleaned dataset
df.to_csv('cleaned_data.csv', index=False)

print("Data cleaning completed and saved as 'cleaned_data.csv'")
