import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\lenna\\OneDrive\\Desktop\\marketing_campaign_analysis\\DigitalAd_dataset.csv")

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

print(df.columns)


# Drop or fill missing values
df.fillna(0, inplace=True)  # Replace missing values with 0

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns (Example: Change 'clicks' to 'Total_Clicks')
df.rename(columns={'clicks': 'Total_Clicks'}, inplace=True)

# Save the cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved as cleaned_data.csv")


print(df.columns)



df.to_csv("cleaned_data.csv", index=False)
print("cleaned_data.csv has been created successfully!")