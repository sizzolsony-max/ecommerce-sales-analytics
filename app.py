import os
import pandas as pd
import matplotlib.pyplot as plt

# 1) CREATE SAMPLE E-COMMERCE DATA
data = {
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "order_date": [
        "2024-01-05", "2024-01-15", "2024-02-02", "2024-02-20",
        "2024-03-05", "2024-03-18", "2024-04-01", "2024-04-22",
        "2024-05-10", "2024-05-25", "2024-06-03", "2024-06-18"
    ],
    "country": [
        "India", "India", "USA", "USA",
        "India", "UK", "India", "USA",
        "UK", "India", "USA", "UK"
    ],
    "product": [
        "Shoes", "T-Shirt", "Shoes", "Jeans",
        "Jeans", "Shoes", "Watch", "Shoes",
        "T-Shirt", "Watch", "Jeans", "Watch"
    ],
    "quantity": [2, 1, 1, 3, 2, 1, 1, 2, 4, 1, 2, 3],
    "price_per_unit": [2000, 800, 2200, 1500, 1600, 2100, 3000, 2100, 900, 3200, 1700, 3200],
}

df = pd.DataFrame(data)

# Convert order_date to datetime and create Year-Month column
df["order_date"] = pd.to_datetime(df["order_date"])
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)

# Calculate revenue
df["revenue"] = df["quantity"] * df["price_per_unit"]

print("First rows of data:")
print(df.head())
print("\nTotal rows:", len(df))
print("\nColumns:", df.columns.tolist())

# 2) BASIC ANALYSIS

# Revenue by month
rev_by_month = df.groupby("year_month")["revenue"].sum().reset_index()
print("\nRevenue by Month:")
print(rev_by_month)

# Revenue by country
rev_by_country = df.groupby("country")["revenue"].sum().reset_index()
print("\nRevenue by Country:")
print(rev_by_country)

# Top products by revenue
rev_by_product = df.groupby("product")["revenue"].sum().reset_index().sort_values(by="revenue", ascending=False)
print("\nRevenue by Product:")
print(rev_by_product)

# 3) CREATE OUTPUTS FOLDER IF NOT EXISTS
os.makedirs("outputs", exist_ok=True)

# 4) PLOTS

# Revenue by month (line chart)
plt.figure()
plt.plot(rev_by_month["year_month"], rev_by_month["revenue"], marker="o")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/revenue_by_month.png")

# Revenue by country (bar chart)
plt.figure()
plt.bar(rev_by_country["country"], rev_by_country["revenue"])
plt.title("Revenue by Country")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_country.png")

# Revenue by product (bar chart)
plt.figure()
plt.bar(rev_by_product["product"], rev_by_product["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_product.png")

print("\nCharts saved in the 'outputs' folder:")
print(" - outputs/revenue_by_month.png")
print(" - outputs/revenue_by_country.png")
print(" - outputs/revenue_by_product.png")
