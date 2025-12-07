import streamlit as st
import pandas as pd

# ---------- 1) CREATE SAMPLE DATA ----------
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
df["order_date"] = pd.to_datetime(df["order_date"])
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)
df["revenue"] = df["quantity"] * df["price_per_unit"]

# ---------- 2) STREAMLIT DASHBOARD UI ----------

st.title("📊 E-commerce Sales Dashboard")
st.write("This dashboard shows revenue trends by **month**, **country**, and **product**.")

# KPIs
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_countries = df["country"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Countries", total_countries)

st.markdown("---")

# Filter by country
all_countries = sorted(df["country"].unique().tolist())
selected_countries = st.multiselect(
    "Filter by Country",
    options=all_countries,
    default=all_countries,
)

filtered_df = df[df["country"].isin(selected_countries)]

# Revenue by Month
rev_by_month = (
    filtered_df.groupby("year_month")["revenue"]
    .sum()
    .reset_index()
    .sort_values("year_month")
)

# Revenue by Country
rev_by_country = (
    filtered_df.groupby("country")["revenue"]
    .sum()
    .reset_index()
    .sort_values("revenue", ascending=False)
)

# Revenue by Product
rev_by_product = (
    filtered_df.groupby("product")["revenue"]
    .sum()
    .reset_index()
    .sort_values("revenue", ascending=False)
)

# ---------- 3) SHOW CHARTS ----------

st.subheader("📆 Revenue by Month")
st.line_chart(rev_by_month.set_index("year_month")["revenue"])

st.subheader("🌍 Revenue by Country")
st.bar_chart(rev_by_country.set_index("country")["revenue"])

st.subheader("🛍️ Revenue by Product")
st.bar_chart(rev_by_product.set_index("product")["revenue"])

st.markdown("---")
st.caption("Sample data dashboard for portfolio / learning purposes.")
