# Task-3
# Sales Data Analysis Report

## Project Overview
This project performs a basic sales data analysis using Python and the Pandas library. 
The goal is to analyze a real-world style sales dataset to calculate total revenue, 
identify the best-selling product, and extract basic statistical insights.

---

## Dataset Description
The dataset (`sales_data.csv`) contains sales transaction details including:
- Product name
- Quantity sold
- Price per unit
- Total sales value

Missing values were handled to ensure accurate analysis.

---

## Tools & Technologies Used
- Python
- Pandas library
- CSV file format

---

## Methodology

### 1. Data Loading
The dataset was loaded using Pandas `read_csv()` function.

### 2. Data Exploration
Basic exploration was performed to understand:
- Number of rows and columns
- Column names
- Data types
- Missing values

### 3. Data Cleaning
- Missing values in the `Total_Sales` column were filled using:
- Duplicate records were removed.

### 4. Data Analysis
The following metrics were calculated:
- Total revenue generated
- Best-selling product based on revenue
- Average sales value
- Highest and lowest sales values

---

## Key Results
- **Total Revenue:** Calculated by summing the `Total_Sales` column
- **Best-Selling Product:** Product with the highest cumulative sales
- **Statistical Insights:** Mean, maximum, and minimum sales values

---

## Conclusion
This analysis demonstrates how Python and Pandas can be used to efficiently process, 
clean, and analyze real-world datasets. The project provides a foundation for more 
advanced data analytics and business intelligence tasks.


