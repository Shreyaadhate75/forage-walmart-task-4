import pandas as pd
import sqlite3

conn = sqlite3.connect("walmart.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shipments (
    product TEXT,
    quantity INTEGER,
    origin TEXT,
    destination TEXT
)
""")

sheet0 = pd.read_excel("data/spreadsheet0.xlsx")
for _, row in sheet0.iterrows():
    cursor.execute("""
    INSERT INTO shipments (product, quantity, origin, destination)
    VALUES (?, ?, ?, ?)
    """, (row['product'], row['quantity'], row['origin'], row['destination']))

sheet1 = pd.read_excel("data/spreadsheet1.xlsx")
sheet2 = pd.read_excel("data/spreadsheet2.xlsx")

combined = pd.merge(sheet1, sheet2, on="shipment_id")

for _, row in combined.iterrows():
    cursor.execute("""
    INSERT INTO shipments (product, quantity, origin, destination)
    VALUES (?, ?, ?, ?)
    """, (row['product'], row['quantity'], row['origin'], row['destination']))

conn.commit()
conn.close()

print("Data inserted successfully!")
