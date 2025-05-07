import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("C:\\Users\\lenna\\OneDrive\\Desktop\\marketing_campaign_analysis\\DigitalAd_dataset.csv")
df.columns = df.columns.str.strip()


# Overview of the dataset
print("Dataset Overview:")
print(df.info())
print("First few rows:")
print(df.head())

print(df["Purchased"].isnull().sum())  # Count missing values

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# Purchase Rate
purchase_rate = df["Purchased"].mean() * 100
print(f"Purchase Rate: {purchase_rate:.2f}% of users made a purchase.")

# Correlation Analysis
correlation_matrix = df[["Min_spent", "Clicks", "Annual_inc", "Age", "Purchased"]].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualization: Spending vs. Clicks
plt.figure(figsize=(8, 5))
plt.scatter(df["Min_spent"], df["Clicks"], alpha=0.5, c=df["Purchased"], cmap="coolwarm")
plt.colorbar(label="Purchased (0 = No, 1 = Yes)")
plt.xlabel("Minimum Spent")
plt.ylabel("Clicks")
plt.title("Spending vs. Clicks")
plt.show()

# Age Distribution
plt.figure(figsize=(8, 5))
df["Age"].hist(bins=20, edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Users")
plt.show()

# Income vs. Purchase Rate
plt.figure(figsize=(8, 5))
df.groupby("Annual_inc")["Purchased"].mean().plot(kind="bar", color="skyblue")
plt.xlabel("Annual Income")
plt.ylabel("Purchase Rate")
plt.title("Income vs. Purchase Likelihood")
plt.xticks(rotation=45)
plt.show()

