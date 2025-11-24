import sqlite3

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

data = [
    ("Laptop", 4, 52000),
    ("Mouse", 15, 450),
    ("Keyboard", 8, 1400),
    ("Monitor", 5, 12000),
    ("Headphones", 12, 1800),
    ("Pendrive 32GB", 20, 500),
    ("Hard Disk 1TB", 6, 3500),
    ("SSD 512GB", 7, 4500),
    ("Webcam", 4, 2500),
    ("Speakers", 10, 2000),
    ("Printer", 3, 15000),
    ("Router", 9, 1800),
    ("Projector", 2, 35000),
    ("Tablet", 5, 25000),
    ("Smartwatch", 12, 5000),
    ("Microphone", 6, 2200),
    ("Graphics Card", 1, 45000),
    ("Motherboard", 3, 7000),
    ("RAM 8GB", 10, 3600),
    ("Cooling Fan", 14, 400)
]

cur.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()
print("sales_data.db created with sample product data!")
