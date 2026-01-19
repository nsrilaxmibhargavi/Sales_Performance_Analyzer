
# 📊 Sales Performance Analyzer

A Python-based data analysis project that turns raw sales data into clear insights, visual reports, and interactive dashboards.  
This project automates the entire flow: data cleaning, KPI calculation, visualization, and report generation.

---

## 🔍 What this project does

The Sales Performance Analyzer takes a sales dataset and answers key business questions:

- How is revenue trending month by month?
- Which products generate the most revenue?
- Which regions perform better?
- What are the overall KPIs (revenue, profit, orders, units, etc.)?

It produces charts, Excel summaries, PDFs, and interactive dashboards in one run.

---

## 📈 Output Preview

### Monthly Revenue Trend
Shows how revenue changes over time and helps identify patterns and growth.
<img width="800" height="495" alt="Screenshot 2026-01-19 161008" src="https://github.com/user-attachments/assets/c87bfaf7-97a8-43b4-aaff-6d0cd9aa4571" />



### Top 10 Products by Revenue
Highlights the highest revenue-generating products.
<img width="800" height="495" alt="Screenshot 2026-01-19 161021" src="https://github.com/user-attachments/assets/2df76fc1-562d-4a48-83f6-65dd615bfd91" />



### Revenue by Region
Compares performance across different regions.
<img width="800" height="495" alt="Screenshot 2026-01-19 161034" src="https://github.com/user-attachments/assets/45484672-99a6-48ac-8423-f8a161f26f99" />



---

## 📁 Generated Reports

After execution, the following files are created in the `output/` folder:

- `monthly.png` – Monthly revenue chart  
- `products.png` – Top products chart  
- `region.png` – Region-wise revenue chart  
- `sales_report.pdf` – Combined PDF report  
- `sales_summary.xlsx` – Excel report with KPIs and summaries  
- `monthly.html` – Interactive monthly revenue dashboard  
- `products.html` – Interactive product dashboard  
- `region.html` – Interactive regional dashboard  

---

## 🧠 KPIs Calculated

The script automatically calculates:

- Total Revenue
- Total Orders
- Total Units Sold
- Average Order Value
- Average Discount
- Total Profit

These KPIs are also exported to Excel for easy sharing and reporting.

---

## ⚙️ Tech Stack

- Python 3.10+
- Pandas, NumPy
- Matplotlib
- Plotly
- XlsxWriter
- Kaggle API

---

## 🚀 How to Run

### 1. Clone the repository
git clone https://github.com/nsrilaxmibhargavi/sales-performance-analyzer.git
cd sales-performance-analyzer

### 2. Install dependencies
pip install pandas numpy matplotlib plotly xlsxwriter kaggle

### 3. Run the project
python main.py


All reports will be generated automatically in the output/ folder.

---

## 📌 Dataset

This project uses the Superstore Sales Dataset from Kaggle.
Make sure your Kaggle API is configured if you want automatic downloading.

---

## ✅ Highlights

End-to-end sales data analysis pipeline

Automatic report generation (PNG, PDF, Excel, HTML)

Clean and reusable Python code structure

Suitable for portfolios, internships, and academic projects

---

## 🧾 Conclusion

This project demonstrates how raw sales data can be transformed into meaningful business insights using Python.
By automating analysis, visualization, and reporting, it reduces manual effort and provides a clear, repeatable workflow for decision-making.
It also serves as a solid example of practical data analysis skills, combining data cleaning, KPI computation, and professional reporting in a single pipeline.
