
import streamlit as st
import sqlite3
import pandas as pd

##Connection to the database
connection = sqlite3.connect("sales_pipeline.db")

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)
st.title("E-Commerce Sales Dashboard")

#setting out the side bar filters
with st.sidebar:
  st.header("Filters")
  year_filter = st.selectbox(
      "Select Year",
      ["All Years", 2023, 2024, 2025]
  )




#Styling the KPI components
st.markdown("""
        <style>
        div[data-testid="stMetric"] {
               background-color: #f5f7f6;
               border: 1px solid #d9e2dc;
               padding: 30px;
               border-radius: 12px;
               box-shadow: 0 2px 6px rgba(0,0,0,0.08);
           }

       [data-testid="stMetricLabel"] p {
        font-size: 15px;

        }

        </style>
""", unsafe_allow_html=True)

if year_filter == "All Years":
    query = """
    SELECT COUNT(*) AS Total_Orders
    FROM sales_data
    """
else:
    query = f"""
    SELECT COUNT(*) AS Total_Orders
    FROM sales_data
    WHERE Year = {year_filter}
    """
result = pd.read_sql(query, connection)


### Total revenue KPI
if year_filter == "All Years":
    Revenue_querry = """
    SELECT SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    """
else:
    Revenue_querry = f"""
    SELECT SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    WHERE Year = {year_filter}
    """
revenue = pd.read_sql(Revenue_querry, connection)

## Total profit
if year_filter == "All Years":
    Profit_querry = """
    SELECT SUM(Profit) AS Total_Profit
    FROM sales_data
    """
else:
    Profit_querry = f"""
    SELECT SUM(Profit) AS Total_Profit
    FROM sales_data
    WHERE Year = {year_filter}
    """

T_Profit = pd.read_sql(Profit_querry, connection)

##Total units sold
if year_filter == "All Years":
    Units_querry = """
    SELECT SUM(Quantity) AS Total_Units_Sold
    FROM sales_data
    """
else:
    Units_querry = f"""
    SELECT SUM(Quantity) AS Total_Units_Sold
    FROM sales_data
    WHERE Year = {year_filter}
    """
T_Units = pd.read_sql(Units_querry, connection)


# Styling the KPI
col1, col2, col3, col4 = st.columns(4) #creating 4 columns for kpi

#Placing each kpi in its own column
with col1:
    st.metric("Total Orders", result.iloc[0, 0])
with col2:
    st.metric("Total Revenue", revenue.iloc[0,0])
with col3:
    st.metric("Total Profit", T_Profit.iloc[0,0])
with col4:
    st.metric("Total Units Sold", T_Units.iloc[0,0])


## Building dashboard charts
colu1, colu2 = st.columns(2)
# Revenue by product
if year_filter == "All Years":
    product_query = """
    SELECT Product_Name, SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    GROUP BY Product_Name
    ORDER BY Total_Revenue DESC
    LIMIT 10
    """
else:
    product_query = f"""
    SELECT Product_Name, SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    WHERE Year = {year_filter}
    GROUP BY Product_Name
    ORDER BY Total_Revenue DESC
    LIMIT 10
    """
product_revenue = pd.read_sql(product_query, connection)

with colu1:
      st.header("Top 5 Products by Gross Sales")
      st.bar_chart(
      product_revenue.set_index("Product_Name")["Total_Revenue"],
      horizontal=True
)


## Most profit by product
if year_filter == "All Years":
    profit_product_query = """
    SELECT Product_Name, SUM(Profit) AS Total_Profit
    FROM sales_data
    GROUP BY Product_Name
    ORDER BY Total_Profit DESC
    LIMIT 10
    """
else:
    profit_product_query = f"""
    SELECT Product_Name, SUM(Profit) AS Total_Profit
    FROM sales_data
    WHERE Year = {year_filter}
    GROUP BY Product_Name
    ORDER BY Total_Profit DESC
    LIMIT 10
    """
product_profit = pd.read_sql(profit_product_query, connection)

with colu2:
  st.header("Top 5 Products by Profit")
  st.bar_chart(
      product_profit.set_index("Product_Name")["Total_Profit"],
      horizontal=True
  )


if year_filter == "All Years":
    year_query = """
    SELECT Year, SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    GROUP BY Year
    ORDER BY Year
    """
else:
    year_query = f"""
    SELECT Year, SUM(Total_Sales) AS Total_Revenue
    FROM sales_data
    WHERE Year = {year_filter}
    GROUP BY Year
    ORDER BY Year
    """
year_revenue = pd.read_sql(year_query, connection)

year_revenue["Year"] = year_revenue["Year"].astype(str)
colu3, colu4 = st.columns(2)
with colu3:
  st.header("Revenue by Year")
  year_revenue["Year"] = year_revenue["Year"].astype(str)

  st.line_chart(
    year_revenue.set_index("Year")["Total_Revenue"]
)


if year_filter == "All Years":
    order_type_query = """
    SELECT High_Value_Order, COUNT(*) AS Order_Count
    FROM sales_data
    GROUP BY High_Value_Order
    """
else:
    order_type_query = f"""
    SELECT High_Value_Order, COUNT(*) AS Order_Count
    FROM sales_data
    WHERE Year = {year_filter}
    GROUP BY High_Value_Order
    """

order_type = pd.read_sql(order_type_query, connection)
with colu4:
  st.subheader("High values VS Normal values")
  st.bar_chart(
      order_type.set_index("High_Value_Order")["Order_Count"],
      horizontal=True
  )


