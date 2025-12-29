import pandas as pd#importing pandas 
df=pd.read_csv("sales_data.csv")#Load daatset
print(df.head())#displaying first five rows 
print("Rows and columns:", df.shape)# shape of the dataset
print("Column names:", df.columns)#column names
print(df.info())# data types for each column and missing value information
print(df.isnull().sum())#checking missing values 
df["Total_Sales"]= df["Total_Sales"].fillna(df["Quantity"]*df["Price"])# filling missing values if any
df=df.drop_duplicates()# removing duplicates 
total_revenue= df["Total_Sales"].sum()#Calculating total revenue 
best_product= df.groupby("Product")["Total_Sales"].sum().idxmax()#Identifying best product with the maximum sale 
#Statistics
average_sales=df["Total_Sales"].mean()#Average sales
highest_sales= df["Total_Sales"].max()#Highest sales 
lowest_sales=df["Total_Sales"].min()#lowest sales
#Display of all the metrics 
print("\n   SALES DATA ANALYSIS REPORT   ")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Average Sale: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{highest_sales:,.2f}")
print(f"Lowest Sale: ₹{lowest_sales:,.2f}")
