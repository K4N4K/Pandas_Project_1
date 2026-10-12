import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("clipkart_ecommerce_data.csv")
print(df)
print(df.head()) # view the first rows
print(df.tail()) #view the last rows
print(df.shape) #check diamensions
# check columns names
print(df.columns)
print(df.dtypes) # check data types
print(df.isnull().sum()) # check missing values
print(df.duplicated().sum()) # chceck duplicates rows
print(df.drop_duplicates())
print(df.describe())
# convert date column
df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"].dt.year)
print(df["Date"].dt.month)
print(df["Product"].unique()) # what products?
print(df["Category"].nunique()) # how many categories?
# find transaction where price are greate than 1000
high_price = df[df["Price"]>1000]
print(high_price)
# Filter By catrgory
clothing = df[df["Category"]=="Clothing"]
print(clothing)
# Multiple condition
result = df[(df["Category"] == "Clothing") & (df["City"] == "Delhi")]
print(result)
# sort revenue
sorted_revenue = df.sort_values("Revenue",ascending = False)
print(sorted_revenue)
# calculate total quantity sold
total_quantity = df["Quantity"].sum()
print(total_quantity)
# best selling product
product_revenue = (df.groupby("Product")["Revenue"].sum().sort_values(ascending = False))
print(product_revenue)
# calculate total revenue for each category
category_revenue = (df.groupby("Category")["Revenue"].sum().sort_values(ascending = False))
print(category_revenue)
# calculate average revenue
average_revenue = df["Revenue"].mean()
print(average_revenue)
# count transaction by category
category_count = df["Category"].value_counts()
print(category_count)
 # create  category level summary table
summary = df.groupby("Category").agg(Total_Revenue=("Revenue","sum"),Average_Revenue=("Revenue","mean"),Total_Quantity=("Quantity","sum"),Transactions=("Product","count"))
print(summary)
# Extract Year
df["Year"] = df["Date"].dt.year
print(df[["Date","Year"]].head())
# Extract Month
df["Month_Name"] = df["Date"].dt.month_name()
print( df["Month_Name"]) 
# Create a monthly Revenue chart
sorted_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
