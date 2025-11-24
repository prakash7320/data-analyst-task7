import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")


query = """
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""


df = pd.read_sql_query(query, conn)
conn.close()


print("\n===== SALES SUMMARY =====")
print(df.to_string(index=False))


plt.figure(figsize=(10, 5))
plt.bar(df["product"], df["revenue"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.title("Revenue by Product")
plt.tight_layout()


plt.savefig("sales_chart.png")
plt.show()
