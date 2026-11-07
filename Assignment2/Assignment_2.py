#Name: Nicole Song
#Date: November 6, 2026

#Assignment: Build an interactive dashboard
#Individual requirement 1: Ask user if they want the results exported to an excel file and what to name the excel file
#Individual requirement 2: Keep track of which analytics have been done, store the results, and add it as a menu item

#Started with Assignment 2 Workshop Ex3 as a base and worked from there

import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

#Function to load the CSV file
def load_csv(filepath):
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"\nCSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        return df
    except Exception as e:
        print("Error reading the CSV file:", e)
        return None

#Function to determine how many initial rows to display
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
        if num_rows == '':
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

#Function to exit the program
def exit_program(data):
    print("Exiting the program...")
    raise SystemExit

menu_options = (
    ("Show the first n rows of sales data", display_data),
    #("Total sales by region and order type", total_by_region_and_type),
    #("Average sales by region with average sales by state and sale type", average_sales_region_state_type),
    #("Sales by customer type and order type by state.", sales_by_customer_and_type),
    #("Total sales quantity and price by region and product", total_sales_by_region_and_product),
    #("Total sales quantity and price by customer type", total_sales_by_customer_type),
    #("Max and min sales price of sales by category", max_min_sales_by_category),
    #("Show the number of employees by region", show_employees_by_region),
    #("Create a custom pivot table", custom_pivot_table),
    ("Exit the program", exit_program),
)

#Function to display the menu and ensure the user enters a valid selection
def display_menu():
    while True:
        print("\nSales Data Menu")
        for option_number, option in enumerate(menu_options, start=1): #DON'T use this code.
            print(f"{option_number}. {option[0]}")

        selection = input("Select an option: ").strip()
        try:
            selection = int(selection)
        except ValueError:
            print("\nInvalid selection. Please enter a menu number.")
            continue

        if 1 <= selection <= len(menu_options):
            return selection

        print(
            f"\nInvalid selection. Please enter a number from 1 to "
            f"{len(menu_options)}."
        )

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
