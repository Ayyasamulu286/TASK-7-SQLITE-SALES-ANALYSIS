# 📊 TASK 7: Python తో SQLite Sales Analysis

> **DataX Labs — Data Analyst Internship**  
> **Task 7:** Get Basic Sales Summary from a Tiny SQLite Database using Python

---

## 🎯 Objective (లక్ష్యం)

Python లోపల SQL ని ఉపయోగించి చిన్న SQLite database నుండి sales సమాచారం (total quantity, total revenue) తీసుకొని, `print` statements మరియు `matplotlib` bar chart ద్వారా display చేయడం.

---

## 📁 Dataset (డేటా గురించి)

`sales_data.db` అనే SQLite database file create చేశాం.  
దాని లో **`sales`** అనే ఒక table ఉంది, దానిలో కింది columns ఉన్నాయి:

| Column   | Type    | వివరణ                    |
|----------|---------|--------------------------|
| id       | INTEGER | Auto Increment Primary Key |
| product  | TEXT    | Product పేరు             |
| quantity | INTEGER | అమ్మిన Quantity          |
| price    | REAL    | ఒక్కో Item Price (₹)     |

### 📦 Sample Data (8 Products):

| Product    | Quantity | Price (₹) |
|------------|----------|-----------|
| Laptop     | 10       | 55,000    |
| Mobile     | 25       | 18,000    |
| Headphones | 40       | 2,500     |
| Tablet     | 15       | 22,000    |
| Smartwatch | 20       | 8,500     |
| Keyboard   | 35       | 1,200     |
| Mouse      | 50       | 800       |
| Monitor    | 12       | 14,000    |

---

## 🔍 SQL Queries (అడిగిన Queries)

### Query 1 — Product-wise Sales Summary:
```sql
SELECT
    product,
    SUM(quantity)         AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
```

**`GROUP BY` అంటే ఏమిటి?**  
ప్రతి product కి సంబంధించిన rows అన్నీ group చేసి, వాటి మొత్తం quantity మరియు revenue calculate చేస్తుంది.

**Revenue Calculate చేయడం ఎలా?**  
`SUM(quantity * price)` — ప్రతి row లో quantity × price multiply చేసి, అన్ని rows కలిపితే total revenue వస్తుంది.

### Query 2 — Overall Business Summary:
```sql
SELECT
    COUNT(DISTINCT product) AS total_products,
    SUM(quantity)           AS total_units_sold,
    SUM(quantity * price)   AS total_revenue
FROM sales
```

---

## 📤 Output (ఫలితాలు)

### Product-wise Summary:
```
product     total_qty   revenue
Laptop          10      550000.0
Mobile          25      450000.0
Tablet          15      330000.0
Smartwatch      20      170000.0
Monitor         12      168000.0
Headphones      40      100000.0
Keyboard        35       42000.0
Mouse           50       40000.0
```

### Overall Business Summary:
```
Total Products    : 8
Total Units Sold  : 207
Total Revenue     : ₹18,50,000.00
```

---

## 📊 Chart Screenshot (చార్ట్ చూపించడం)

రెండు bar charts తయారు చేశాం:

1. **Revenue by Product** — ఏ product ఎంత revenue ఇచ్చింది
2. **Quantity Sold by Product** — ఏ product ఎంత quantity అమ్మింది

![Sales Chart](screenshots/chart.png)

Charts `matplotlib` తో తయారు చేసి `sales_chart.png` గా save చేశాం.

---

## 🛠️ Tools & Libraries వాడినవి

| Tool / Library | దేనికి వాడాం |
|----------------|--------------|
| `sqlite3`      | Database connect చేయడానికి (Python built-in) |
| `pandas`       | SQL query result ని DataFrame లో load చేయడానికి |
| `matplotlib`   | Bar charts తయారు చేయడానికి |

---

## 🚀 ఎలా Run చేయాలి?

```bash
# Step 1: Repository clone చేయండి
git clone https://github.com/YOUR_USERNAME/TASK-7-SQLITE-SALES-ANALYSIS.git
cd TASK-7-SQLITE-SALES-ANALYSIS

# Step 2: Libraries install చేయండి
pip install pandas matplotlib

# Step 3: Script run చేయండి
python task7.py
```

---

## 💡 Interview Questions & Answers

**Q1: Python ని Database కి ఎలా connect చేశారు?**  
`sqlite3` module వాడాం: `conn = sqlite3.connect("sales_data.db")` — ఇది file లేకపోతే automatically create చేస్తుంది.

**Q2: ఏ SQL Query run చేశారు?**  
`SELECT product, SUM(quantity), SUM(quantity * price) FROM sales GROUP BY product` — product వారీగా total quantity మరియు revenue తీసుకున్నాం.

**Q3: GROUP BY ఏం చేస్తుంది?**  
Same product name ఉన్న అన్ని rows ని ఒక group లో చేర్చి, ఆ group కి aggregate functions (SUM, COUNT) apply చేస్తుంది.

**Q4: Revenue ఎలా calculate చేశారు?**  
`SUM(quantity * price)` — quantity మరియు price multiply చేసి, అన్ని transactions మొత్తం కలిపాం.

**Q5: Result ని ఎలా visualize చేశారు?**  
`matplotlib` తో bar charts తయారు చేశాం — revenue chart మరియు quantity chart రెండూ ఒకే figure లో display చేశాం.

**Q6: Pandas ఏం చేస్తుంది?**  
`pd.read_sql_query()` వాడి SQL result ని DataFrame లో load చేస్తుంది. DataFrame వల్ల data ని table format లో easily print, filter, analyze చేయవచ్చు.

**Q7: SQL ని Python లో వాడడం వల్ల ఏమి లాభం?**  
Database query + Python data processing + visualization అన్నీ ఒకే script లో చేయవచ్చు. Automation సులభం అవుతుంది.

**Q8: DB Browser for SQLite లో కూడా ఇదే query run చేయవచ్చా?**  
అవును! DB Browser for SQLite లో `sales_data.db` file open చేసి, "Execute SQL" tab లో అదే query paste చేసి run చేయవచ్చు.

---

## 📂 Project Structure

```
TASK-7-SQLITE-SALES-ANALYSIS/
│
├── sales_data.db       ← SQLite Database file
├── task7.py            ← Main Python Script
├── sales_chart.png     ← Generated Bar Chart
├── README.md           ← This file
└── screenshots/
    ├── output.png      ← Terminal output screenshot
    └── chart.png       ← Chart screenshot
```

---

## ✅ Conclusion (నిర్ణయం)

ఈ task లో మేము:
- Python తో SQLite database create చేసి data insert చేశాం
- SQL queries వాడి product-wise sales summary తీశాం  
- `GROUP BY` తో aggregate calculations చేశాం
- `pandas` తో data ని DataFrame లో load చేశాం
- `matplotlib` తో professional bar charts తయారు చేశాం

ఇది real-world data analysis కి ఒక solid foundation ని ఇస్తుంది — database, SQL, Python, మరియు visualization అన్నీ కలిపి వాడడం నేర్చుకున్నాం! 🎉

---

*Submitted by: [మీ పేరు]*  
*Internship: DataX Labs — Data Analyst Internship*
