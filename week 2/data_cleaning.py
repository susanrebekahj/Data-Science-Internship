import pandas as pd
import seaborn as sns

# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Show initial dataset info
print("Initial Dataset Info:")
print(df.info())

# Handle missing values
df.fillna({'age': df['age'].mean(), 'embarked': df['embarked'].mode()[0]}, inplace=True)
df.dropna(subset=['fare'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Show cleaned dataset info
print("\nCleaned Dataset Info:")
print(df.info())

# Save the cleaned data to a CSV file
df.to_csv("cleaned_titanic.csv", index=False)
print("\nCleaned data saved as 'cleaned_titanic.csv'")
