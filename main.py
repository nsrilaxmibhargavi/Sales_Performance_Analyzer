import os
import sys
import subprocess
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.backends.backend_pdf import PdfPages

# ================= CONFIG ===================
DATASET = r"D:\Sale_Performance_analyser\archive"
FILENAME = "Sample - Superstore.csv"
DATA_DIR = "data"
OUTPUT_DIR = "output"

Path(DATA_DIR).mkdir(exist_ok=True)
Path(OUTPUT_DIR).mkdir(exist_ok=True)

# ===========================================
def download_data():
    if not os.path.exists(f"{DATA_DIR}/{FILENAME}"):
        print("⬇️ Downloading Kaggle dataset...")
        subprocess.call(
            f'kaggle datasets download -d {DATASET} -f "{FILENAME}" -p {DATA_DIR} --unzip',
            shell=True
        )
    else:
        print("✅ Dataset already exists")

# ===========================================
def load_and_clean():
    df = pd.read_csv(
        f"{DATA_DIR}/{FILENAME}",
        encoding="latin1"
    )
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    df['order_date'] = pd.to_datetime(df['order_date'])
    df['sales'] = pd.to_numeric(df['sales'])
    df['quantity'] = pd.to_numeric(df['quantity'])
    df['profit'] = pd.to_numeric(df['profit'])

    df['month'] = df['order_date'].dt.to_period("M").astype(str)
    df['year'] = df['order_date'].dt.year
    df['revenue'] = df['sales']
    df['unit_price'] = df['revenue'] / df['quantity']

    return df

# ===========================================
def compute_kpis(df):
    return {
        "Total Revenue": df['revenue'].sum(),
        "Total Orders": len(df),
        "Total Units": df['quantity'].sum(),
        "Average Order Value": df['revenue'].sum() / len(df),
        "Average Discount": df['discount'].mean(),
        "Total Profit": df['profit'].sum()
    }

# ===========================================
def aggregate(df):
    monthly = df.groupby("month")['revenue'].sum().reset_index()
    region = df.groupby("region")['revenue'].sum().reset_index()
    product = df.groupby("product_name")['revenue'].sum().reset_index().sort_values("revenue", ascending=False).head(10)
    return monthly, region, product

# ===========================================
def save_charts(monthly, region, product):
    # Monthly
    plt.figure(figsize=(10,5))
    plt.plot(monthly['month'], monthly['revenue'], marker='o')
    plt.xticks(rotation=45)
    plt.title("Monthly Revenue")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/monthly.png")
    plt.close()

    # Region
    plt.figure(figsize=(8,5))
    plt.bar(region['region'], region['revenue'])
    plt.title("Revenue by Region")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/region.png")
    plt.close()

    # Products
    plt.figure(figsize=(10,5))
    plt.bar(product['product_name'], product['revenue'])
    plt.xticks(rotation=75)
    plt.title("Top Products")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/products.png")
    plt.close()

# ===========================================
def save_pdf():
    with PdfPages(f"{OUTPUT_DIR}/sales_report.pdf") as pdf:
        for img in ["monthly.png", "region.png", "products.png"]:
            fig = plt.figure()
            plt.imshow(plt.imread(f"{OUTPUT_DIR}/{img}"))
            plt.axis("off")
            pdf.savefig(fig)
            plt.close()

# ===========================================
def save_excel(monthly, region, product, kpis):
    with pd.ExcelWriter(f"{OUTPUT_DIR}/sales_summary.xlsx", engine="xlsxwriter") as writer:
        monthly.to_excel(writer, sheet_name="Monthly", index=False)
        region.to_excel(writer, sheet_name="Region", index=False)
        product.to_excel(writer, sheet_name="Top Products", index=False)
        pd.DataFrame([kpis]).to_excel(writer, sheet_name="KPIs", index=False)
        # ===========================================
def show_dashboard(monthly, region, product):
    fig1 = px.line(monthly, x="month", y="revenue", title="Monthly Revenue")
    fig2 = px.bar(region, x="region", y="revenue", title="Revenue by Region")
    fig3 = px.bar(product, x="product_name", y="revenue", title="Top Products")

    fig1.write_html(f"{OUTPUT_DIR}/monthly.html")
    fig2.write_html(f"{OUTPUT_DIR}/region.html")
    fig3.write_html(f"{OUTPUT_DIR}/products.html")

    print("🌐 Interactive dashboard saved in output folder")

# ===========================================
def main():
    print("\n🚀 SALES PERFORMANCE ANALYSER\n")
    download_data()
    df = load_and_clean()

    kpis = compute_kpis(df)
    monthly, region, product = aggregate(df)

    print("\n📊 KPIs")
    for k,v in kpis.items():
        print(f"{k}: {v:,.2f}")

    save_charts(monthly, region, product)
    save_pdf()
    save_excel(monthly, region, product, kpis)
    show_dashboard(monthly, region, product)

    print("\n✅ Analysis complete!")
    print("📂 Reports saved in output/")

# ===========================================
if __name__ == "__main__":
    main()
