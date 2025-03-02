import pandas as pd

df = pd.read_csv("data.csv")


print("First 5 rows:\n", df.head())


print("\nDataset Statistics:\n", df.describe())
