
import pandas as pd

df = pd.read_csv("C:\\Users\\lenna\\OneDrive\\Desktop\\marketing_campaign_analysis\\cleaned_data.csv")
print(df.columns)  # Print column names


df.columns = df.columns.str.strip()
print(df.columns)