import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = sns.load_dataset("iris")

# Create histograms for numerical columns
df.hist(figsize=(10, 6))
plt.suptitle("Histograms of Numerical Columns")
plt.tight_layout()
plt.show()

# Create box plots for numerical columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("Box Plot of Numerical Columns")
plt.show()

# Heatmap to visualize correlations
plt.figure(figsize=(8, 6))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
