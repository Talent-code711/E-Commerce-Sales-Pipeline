import pandas as pd
import numpy as np
import sqlite3



def validate_data(df):
    errors = []

    if df.isnull().sum().sum() > 0:
        errors.append("Missing values found")

    if df.duplicated().any():
        errors.append("Duplicate rows found")

    if (df["Quantity"] <= 0).any():
        errors.append("Invalid quantity found")

    if (df["Unit_Price"] <= 0).any():
        errors.append("Invalid price found")

    if ((df["Discount_Percent"] < 0) |
        (df["Discount_Percent"] > 100)).any():
        errors.append("Invalid discount found")

    if (df["Shipping_Cost"] < 0).any():
        errors.append("Invalid shipping cost found")

    if (df["Total_Sales"] < 0).any():
        errors.append("Invalid total sales found")

    return errors




def run_pipeline():
  print("Pipeline started")

  #Extract
  df = pd.read_csv("global_ecommerce_sales.csv")
  print("Data extracted")
  print(f"Number of Rows: {len(df)}")
  
  #Validation
  errors = validate_data(df)
  if errors:
    print("Validation failed")
    print(errors)
    return
  print("Validation completed")

  #Transformation
  df["Order_Date"] = pd.to_datetime(df["Order_Date"])
  df["Year"] = df["Order_Date"].dt.year
  df["Month"] = df["Order_Date"].dt.month
  df["Month_Name"] = df["Order_Date"].dt.month_name()
  df["Profit_Margin"] = (df["Profit"] / df["Total_Sales"] * 100)
  df["Profit_Status"] = np.where(df["Profit"] >= 0, "Profit", "Loss")
  df["Sales_Per_Unit"] = df["Total_Sales"] / df["Quantity"]
  df["High_Value_Order"] = np.where(df["Total_Sales"] >= 500, "Yes", "No")
  print("Transfomation copleted")

  # Load
  connection = sqlite3.connect("Sales_Pipeline.db")
  df.to_sql("sales_data", connection,
          if_exists="replace", index=False)
  connection.close()
  print("Data loaded into database")

  ##lets doble check our database
  connection = sqlite3.connect("sales_pipeline.db")
  check = pd.read_sql(
    "SELECT COUNT(*) AS total_rows FROM sales_data",
    connection
)
  print(check)

  connection.close()
  
if __name__ == "__main__":
    run_pipeline()