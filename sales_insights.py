import pandas as pd

import pandas as pd

# df = pd.read_csv("Sales_April_2019.csv").head()
# print(df)
import glob

# files = glob.glob("*.csv")
# print(files)

# for f in files:
#     df = pd.read_csv(f)
#     print(f, df.shape)

# import pandas as pd
# import glob

# files = glob.glob("*.csv")

# for f in files:
#     df = pd.read_csv(f)
#     print(f)


import pandas as pd
import glob

files = glob.glob("*.csv")
df = pd.concat([pd.read_csv(l) for l in files], ignore_index=True)

df = df.rename(columns={
    "Order ID": "Order_id",
    "Quantity Ordered": "Quantity_ordered",
    "Price Each": "Price_each",
    "Order Date": "Order_date",
    "Purchase Address": "Purchase_address"
})
# print(df)


# print(df["Order_date"].head())
df = df[df["Order_date"] != "Order Date"]

df["Order_date"] = pd.to_datetime(df["Order_date"])
df["Month"] = df["Order_date"].dt.month
# print(df)



df["Quantity_ordered"] = pd.to_numeric(df["Quantity_ordered"])
df["Price_each"] = pd.to_numeric(df["Price_each"])

df = df.dropna(subset=["Order_date"])
print(df)


df["Sales"]=df["Quantity_ordered"]*df["Price_each"]
# print(df)
# print(df.groupby("Month")["Sales"].sum())


df = df[df["Month"] != 1]
# 👉 “I removed inconsistent January records to maintain uniform monthly analysis”
print(df)
# print(df["Month"].unique())
monthly_sales = df.groupby("Month")["Sales"].sum().sort_values(ascending=False)
print(monthly_sales)
print(monthly_sales.idxmax())
print(monthly_sales.idxmin())



bestproduct=df.groupby("Product")["Sales"].sum().sort_values()
print(bestproduct)
# Best::::iPhone, Macbook Pro Laptop    
# Worst:::AAA Batteries (4-pack), AA Batteries (4-pack)



df["Day"]=df["Order_date"].dt.day_name()
print(df)

daywisetotal=df.groupby("Day")["Sales"].sum()
print(daywisetotal)
# Tuesday(1)



df["City"] = df["Purchase_address"].str.split(",").str[1].str.strip()
print(df)

print(df.groupby("City")["Sales"].sum().sort_values())
# Best---San Francisco ,Los Angeles,
# Worst---Austin,Portland,

print(df["Price_each"].max())
print(df["Price_each"].min())
# Most expensive product price:-1700
# Cheapest Product Price:-2.99


Individual_sold=df.groupby("Product")["Quantity_ordered"].sum().sort_values(ascending=False)
print(Individual_sold)

# 🏆 Top selling (quantity wise):
# AAA Batteries
# AA Batteries
# USB-C Cable


# Final Insights:----
# December had the highest sales among all months. 
# October and November also showed strong performance. 
# iPhone and MacBook Pro generated the highest revenue. 

# AAA Batteries and AA Batteries were the most sold products. 
# Charging cables and accessories also had high sales volume. 

# San Francisco generated the highest sales. 
# Los Angeles also performed strongly. 
# Austin and Portland had comparatively lower sales. 

# Most expensive product price: 1700. 
# Cheapest product price: 2.99 

# SUMMARY----------->>>>>>>>>>
👉 # “I performed end-to-end sales analysis using Python, # and identified key trends in monthly performance, product contribution, and geographic sales distribution.”
