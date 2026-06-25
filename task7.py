# ============================================================
# TASK 7: Get Basic Sales Summary from a Tiny SQLite Database
# Data Analyst Internship - DataX Labs
# ============================================================

import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ─────────────────────────────────────────────
# STEP 1: Create SQLite Database & Insert Data
# ─────────────────────────────────────────────
print("=" * 55)
print("   TASK 7: SQLite Sales Analysis using Python")
print("=" * 55)

# Connect to database (creates file if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        product  TEXT,
        quantity INTEGER,
        price    REAL
    )
""")

# Clear old data (so we don't duplicate on re-run)
cursor.execute("DELETE FROM sales")

# Insert sample sales data
sales_records = [
    ("Laptop",     10, 55000.00),
    ("Mobile",     25, 18000.00),
    ("Headphones", 40,  2500.00),
    ("Tablet",     15, 22000.00),
    ("Smartwatch", 20,  8500.00),
    ("Keyboard",   35,  1200.00),
    ("Mouse",      50,   800.00),
    ("Monitor",    12, 14000.00),
]

cursor.executemany(
    "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
    sales_records
)
conn.commit()
print("\n✅ Database 'sales_data.db' created and data inserted successfully!\n")

# ─────────────────────────────────────────────
# STEP 2: SQL Query 1 — Sales Summary
# ─────────────────────────────────────────────
query1 = """
    SELECT
        product,
        SUM(quantity)           AS total_qty,
        SUM(quantity * price)   AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
"""

df = pd.read_sql_query(query1, conn)

print("─" * 55)
print("  📊 SALES SUMMARY (Product-wise)")
print("─" * 55)
print(df.to_string(index=False))
print("─" * 55)

# ─────────────────────────────────────────────
# STEP 3: SQL Query 2 — Overall Totals
# ─────────────────────────────────────────────
query2 = """
    SELECT
        COUNT(DISTINCT product)  AS total_products,
        SUM(quantity)            AS total_units_sold,
        SUM(quantity * price)    AS total_revenue
    FROM sales
"""

df_total = pd.read_sql_query(query2, conn)

print("\n  🧾 OVERALL BUSINESS SUMMARY")
print("─" * 55)
print(f"  Total Products    : {int(df_total['total_products'][0])}")
print(f"  Total Units Sold  : {int(df_total['total_units_sold'][0])}")
print(f"  Total Revenue     : ₹{float(df_total['total_revenue'][0]):,.2f}")
print("─" * 55)

conn.close()

# ─────────────────────────────────────────────
# STEP 4: Bar Chart — Revenue by Product
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Sales Analysis Dashboard", fontsize=16, fontweight='bold', color='#2C3E50')

colors = ['#3498DB', '#E74C3C', '#2ECC71', '#F39C12',
          '#9B59B6', '#1ABC9C', '#E67E22', '#34495E']

# Chart 1: Revenue Bar Chart
bars = axes[0].bar(df['product'], df['revenue'], color=colors, edgecolor='white', linewidth=0.8)
axes[0].set_title('Revenue by Product (₹)', fontsize=13, fontweight='bold', pad=12)
axes[0].set_xlabel('Product', fontsize=11)
axes[0].set_ylabel('Revenue (₹)', fontsize=11)
axes[0].tick_params(axis='x', rotation=30)
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'₹{x/1000:.0f}K'))
axes[0].grid(axis='y', alpha=0.3, linestyle='--')
axes[0].set_facecolor('#F8F9FA')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    axes[0].annotate(f'₹{height/1000:.0f}K',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=8, fontweight='bold')

# Chart 2: Quantity Sold Bar Chart
bars2 = axes[1].bar(df['product'], df['total_qty'], color=colors, edgecolor='white', linewidth=0.8)
axes[1].set_title('Total Quantity Sold by Product', fontsize=13, fontweight='bold', pad=12)
axes[1].set_xlabel('Product', fontsize=11)
axes[1].set_ylabel('Quantity Sold (Units)', fontsize=11)
axes[1].tick_params(axis='x', rotation=30)
axes[1].grid(axis='y', alpha=0.3, linestyle='--')
axes[1].set_facecolor('#F8F9FA')

for bar in bars2:
    height = bar.get_height()
    axes[1].annotate(f'{int(height)} units',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 4), textcoords="offset points",
                     ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("sales_chart.png", dpi=150, bbox_inches='tight', facecolor='white')
print("\n  ✅ Chart saved as 'sales_chart.png'")
print("=" * 55)
print("  🎉 Task 7 Completed Successfully!")
print("=" * 55)
