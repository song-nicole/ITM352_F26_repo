#Create a data frame from a CSV file and create a pivot table to aggregate sales by region and order type

import pandas as pd
import numpy as np
import ssl

#https is more secure than http and hackers tend to use http to hack
#the statement below bypasses the SSL certificate verification to allow the code to run without errors
ssl._create_default_https_context = ssl._create_unverified_context

#Tell pandas to print all columns when displaying a dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'
try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip') #Engine is what python uses to -- the file
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', format='%Y-%m-%d') #Converts the order_date column to datetime format, if it fails it will return NaT
    #print(df.head())

    #Calculate sales total per row for later use in the pivot table
    df['sales'] = df['quantity'] * df['unit_price']

    #Create a pivot table aggregating sales by region and order_type
    #in excel, you would need to create a few more columns and sumif statements
    pivot_table = pd.pivot_table(df, 
                                 values='sales', 
                                 index='customer_state', 
                                 columns=['customer_type', 'order_type'], 
                                 aggfunc='mean', 
                                 margins=True,
                                 margins_name='Average Sales')
    print(pivot_table)

except Exception as e:
    print("Error reading CSV file:", e)
