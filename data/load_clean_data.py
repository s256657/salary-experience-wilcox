import pandas as pd
import sqlite3
import os

# --- File paths ---
csv_path = "data/Salary_Data_Cleaned.csv"
db_path = "data/salary_data_clean.db"  # database will be created here if it doesn't exist

# --- Load CSV into pandas DataFrame ---
df = pd.read_csv(csv_path)

# --- Connect to (or create) SQLite database ---
conn = sqlite3.connect(db_path)

# --- Write the DataFrame to a table in the database ---
table_name = "salary_data_clean"

# if_exists options:
#   'fail' -> raises error if table exists
#   'replace' -> drops table and recreates it
#   'append' -> adds rows to existing table
df.to_sql(table_name, conn, if_exists='replace', index=False)

# --- Verify the data was inserted ---
preview = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", conn)
print("✅ Data loaded successfully! Here's a preview:")
print(preview)

# --- Close connection ---
conn.close()