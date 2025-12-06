# E-commerce Sales Analytics (Python)

This project is a simple **E-commerce Sales Analysis** built with Python.  
It uses a small sample dataset to show how a data analyst can:

- Calculate **revenue** from orders  
- Analyze revenue by **month**, **country**, and **product**
- Create **visual charts** for business insights

---

## 🔍 What the script does

File: `analysis.py`

1. Creates a sample dataset with:
   - `order_id`
   - `order_date`
   - `country`
   - `product`
   - `quantity`
   - `price_per_unit`
2. Converts `order_date` to a proper date and extracts `year_month`
3. Calculates a new column:  
   `revenue = quantity * price_per_unit`
4. Computes:
   - Revenue by **month**
   - Revenue by **country**
   - Revenue by **product**
5. Saves 3 charts to the `outputs/` folder:
   - `revenue_by_month.png`
   - `revenue_by_country.png`
   - `revenue_by_product.png`

---

## 📊 How to Run

1. Install dependencies:

```bash
pip install pandas matplotlib
