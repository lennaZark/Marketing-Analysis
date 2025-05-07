import sqlite3
import pandas as pd # type: ignore

def create_database():
    conn = sqlite3.connect("ads_data.db")  # Create or connect to database
    cursor = conn.cursor()
    
    # Create table with columns matching your dataset
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Cust_ID TEXT,
        First_timer INTEGER,
        Min_spent REAL,
        Clicks INTEGER,
        Annual_inc REAL,
        Age INTEGER,
        Purchased INTEGER
    )
    """)
    
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("ads_data.db")
    cursor = conn.cursor()
    
    # Load cleaned data (update filename if needed)
    df = pd.read_csv("C:\\Users\\lenna\\OneDrive\\Desktop\\marketing_campaign_analysis\\cleaned_data.csv")

    # Insert data into SQL
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO Ads (Cust_ID, First_timer, Min_spent, Clicks, Annual_inc, Age, Purchased) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
            (row["Cust_ID"], row["First_timer"], row["Min_spent"], row["Clicks"], 
             row["Annual_inc"], row["Age"], row["Purchased"]))

    conn.commit()
    conn.close()

# Run functions
create_database()
insert_data()
print("Data inserted into ads_data.db")