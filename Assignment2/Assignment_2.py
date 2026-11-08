#Name: Nicole Song
#Date: November 7, 2026

#Assignment: Build an interactive dashboard
#Individual requirement 1: Ask user if they want the results exported to an excel file and what to name the excel file
#Individual requirement 2: Keep track of which analytics have been done, store the results, and add it as a menu item

#Started with Assignment 2 Workshop Ex3 as a base and worked from there
#Incorporated parts of Assignment 2 Workshop Ex4

import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

#To display all rows and columns of data
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#Function to load the CSV file
def load_csv(filepath):
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time #To log the time it took for the file to load
        df['sales'] = df['quantity'] * df['unit_price'] #Created a sales column for total sales

        print(f"\nCSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows in the CSV file: {len(df)}")
        print(f"The columns in the CSV file include information on: {df.columns.tolist()}")
        print("\n*** Some lines of data may have been skipped due to bad data and some analytics may not work.")
        print("*** Some of the data may be wrapped to fit the screen.")
        return df
    
    except Exception as e:
        print("\nError reading the CSV file:", e)
        return None

#Menu option 1
#Function to determine how many initial rows to display and navigate invalid inputs
def display_data(data):
    while True:
        print("\nHow many rows of data would you like to see?")
        print(f"   Please enter a whole number from 1 to {len(data)}.")
        print("   For all rows, enter 'all'.")
        print("   To display no rows, press Enter.")
        num_rows = input("\nNumber of rows: ").strip().lower()

        if num_rows == 'all':
            num_rows = len(data)
            return
        if num_rows == '' or num_rows == "0":
            return

        try:
            num_rows = int(num_rows)
        except ValueError:
            print("\nInvalid input. Please enter a whole number or 'all'.")
            continue

        if num_rows < 0:
            print("\nInvalid input. Please enter a non-negative number.")
            continue

        if num_rows > len(data):
            print(f"\nRequested {num_rows} rows, but only {len(data)} rows are available.")
            continue

        print(data.head(num_rows))
        return

#Menu option 2
#Function to calculate total sales by region and order type
def total_by_region_and_type(data):
    print("\n\nTotal sales by region and order type:\n")
    pivot_table = pd.pivot_table(data, index='sales_region', columns='order_type', values='sales', aggfunc='sum', fill_value=0)
    print(pivot_table)
    return

#Menu option 3
#Function to calculate average sales by region with average sales by state and order type
def average_sales_region_state_type(data):
    print("\n\nAverage sales by region with average sales by state and order type:\n")
    pivot_table = pd.pivot_table(data, index='sales_region', columns=['customer_state', 'order_type'], values='sales', aggfunc='mean', fill_value=0)
    print(pivot_table)
    return

#Menu option 4
#Function to calculate sales by customer type and order type by state
def sales_by_customer_and_type(data):
    print("\n\nSales by customer type and order type by state:\n")
    pivot_table = pd.pivot_table(data, index=['customer_state', 'customer_type', 'order_type'], values='sales', aggfunc='sum', fill_value=0)
    print(pivot_table)
    return

#Menu option 5
#Function to calculate total sales quantity and price by region and product
def total_sales_by_region_and_product(data):
    print("\n\nTotal sales quantity and price by region and product:\n")
    pivot_table = pd.pivot_table(data, index=['sales_region', 'produce_name'], values=['quantity', 'unit_price'], aggfunc='sum', fill_value=0)
    print(pivot_table)
    return

#Menu option 6
#Function to calculate total sales quantity and price by customer type
def total_sales_by_customer_type(data):
    print("\n\nTotal sales quantity and price by customer type:\n")
    pivot_table = pd.pivot_table(data, index=['order_type', 'customer_type'], values=['quantity', 'unit_price'], aggfunc='sum', fill_value=0)
    print(pivot_table)
    return

#Menu option 7
#Function to calculate max and min sales price of sales by category
def max_min_sales_by_category(data):
    print("\n\nMaximum and minimum sales price of sales by category:\n")
    pivot_table = pd.pivot_table(data, index='product_category', values='unit_price', aggfunc=['max', 'min'], fill_value=0)
    print(pivot_table)
    return

#Menu option 8
#Function to show the number of employees by region
def employees_by_region(data):
    print("\n\nNumber of unique employees by region:\n")
    pivot_table = pd.pivot_table(data, index='sales_region', values='employee_id', aggfunc='count', fill_value=0)
    print(pivot_table)
    return

#Menu option 9
#Functions that allow the user to create a custom pivot table
#Custom pivot table function 1 - used to get the user's selection from a list of options and navigate invalid inputs
def get_user_selection(options, prompt):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            return []

        try:
            indices = [int(i.strip()) for i in choice.split(",")]
            if any(index < 1 or index > len(options) for index in indices):
                raise IndexError
            selected = [options[index - 1] for index in indices]
        except (ValueError, IndexError):
            print("\nInvalid selection. Please enter valid option number(s).")
            continue

        if len(set(selected)) != len(selected):
            print("\nPlease do not select the same option more than once.")
            continue
        return selected

#Custom pivot table function 2 - used to generate the custom pivot table with user selected information
def custom_pivot_table(data):
    row_options = list(data.columns)
    while True:
        rows = get_user_selection(row_options, "\n\nSelect rows: ")
        if rows:
            break
        print("\nAt least one row selection is required.")

    col_options = row_options
    col_options = [col for col in col_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (press Enter to skip): ")

    value_options = list(data.select_dtypes(include=["number"]).columns)
    if not value_options:
        print("\nNo numeric columns are available for aggregation.")
        return
    while True:
        values = get_user_selection(value_options, "\n\nSelect values: ")
        if values:
            break
        print("\nAt least one value selection is required.")

    agg_options = ["sum", "mean", "count"]
    while True:
        selected_aggregations = get_user_selection(agg_options, "\n\nSelect an aggregation function: ")
        if len(selected_aggregations) == 1:
            agg_func = selected_aggregations[0]
            break
        print("\nSelect exactly one aggregation function.")

    pivot_table = pd.pivot_table(data, index=rows, columns=cols if cols else None, values=values, aggfunc=agg_func)
    
    print("\nYour Custom Pivot Table:\n")
    print(pivot_table)

#Menu option 10
#Function to exit the program
def exit_program(data):
    print("\nExiting the program...")
    print("You have successfully exited the program.\n")
    raise SystemExit

menu_options = (
    ("Show the first n rows of sales data", display_data),
    ("Total sales by region and order type", total_by_region_and_type),
    ("Average sales by region with average sales by state and order type", average_sales_region_state_type),
    ("Sales by customer type and order type by state.", sales_by_customer_and_type),
    ("Total sales quantity and price by region and product", total_sales_by_region_and_product),
    ("Total sales quantity and price by customer type", total_sales_by_customer_type),
    ("Maximum and minimum sales price of sales by category", max_min_sales_by_category),
    ("Show the number of employees by region", employees_by_region),
    ("Create a custom pivot table", custom_pivot_table),
    ("Exit the program", exit_program),
)

#Function to display the menu and ensure the user enters a valid selection
def display_menu():
    while True:
        print("\nSales Data Menu")
        for option_number, option in enumerate(menu_options, start=1): #Number the menu options
            print(f"{option_number}. {option[0]}")

        selection = input("Select an option: ").strip()
        try:
            selection = int(selection)
        except ValueError:
            print("\nInvalid selection. Please enter a menu number.")
            continue

        if 1 <= selection <= len(menu_options):
            return selection

        print(f"\nInvalid selection. Please enter a number from 1 to {len(menu_options)}.")

#Main loop
def main():
    csv_file = ("https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K")
    print(f"\nLoading CSV file from: {csv_file}")
    print("Please wait...")
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    while True:
        selection = display_menu()
        menu_options[selection - 1][1](sales_data)

if __name__ == "__main__":
    main()
