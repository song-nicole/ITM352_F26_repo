import pandas as pd
import ssl
import time


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context


def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None


def display_initial_rows(data):
    """Prompt for and display the requested number of initial DataFrame rows."""
    while True:
        num_rows = input(
            "\nHow many initial rows would you like to see? Please enter a whole number or 'all' for all rows."
        ).strip().lower()

        if num_rows == 'all':
            print(data)
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


def exit_program(data):
    """Exit the program cleanly."""
    print("Exiting the program.")
    raise SystemExit


def show_employees_by_region(data):
    """Display the number of unique employees by region and order type."""
    pivot_table = pd.pivot_table(
        data,
        values="employee_id",
        index="sales_region",
        columns="order_type",
        aggfunc=pd.Series.nunique,
        fill_value=0,
        margins=True,
        margins_name="Total Employees",
    )
    print(pivot_table)


def get_user_selection(options, prompt):
    """Return the options selected by their comma-separated menu numbers."""
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        choice = input(
            "Enter the number(s) of your choice(s), separated by commas: "
        ).strip()
        if not choice:
            return []

        try:
            indices = [int(i.strip()) for i in choice.split(",")]
            if any(index < 1 or index > len(options) for index in indices):
                raise IndexError
            selected = [options[index - 1] for index in indices]
        except (ValueError, IndexError):
            print("Invalid selection. Please enter valid option number(s).")
            continue

        if len(set(selected)) != len(selected):
            print("Please do not select the same option more than once.")
            continue
        return selected


def generate_custom_pivot_table(data):
    """Guide the user through creating and displaying a custom pivot table."""
    row_options = list(data.columns)
    while True:
        rows = get_user_selection(row_options, "Select rows:")
        if rows:
            break
        print("At least one row selection is required.")

    col_options = row_options
    col_options = [col for col in col_options if col not in rows]
    cols = get_user_selection(
        col_options,
        "Select columns (press Enter to skip):",
    )

    value_options = list(data.select_dtypes(include=["number"]).columns)
    if not value_options:
        print("No numeric columns are available for aggregation.")
        return
    while True:
        values = get_user_selection(value_options, "Select values:")
        if values:
            break
        print("At least one value selection is required.")

    agg_options = ["sum", "mean", "count"]
    while True:
        selected_aggregations = get_user_selection(
            agg_options,
            "Select an aggregation function:",
        )
        if len(selected_aggregations) == 1:
            agg_func = selected_aggregations[0]
            break
        print("Select exactly one aggregation function.")

    pivot_table = pd.pivot_table(
        data,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func,
    )
    print(pivot_table)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Exit the program", exit_program),
)


def display_menu():
    """Display the menu and return the user's valid 1-based selection."""
    while True:
        print("\nSales Data Menu")
        for option_number, (description, _) in enumerate(menu_options, start=1): #DON'T use this code.
            print(f"{option_number}. {description}")

        selection = input("Select an option: ").strip()
        try:
            selection = int(selection)
        except ValueError:
            print("Invalid selection. Please enter a menu number.")
            continue

        if 1 <= selection <= len(menu_options):
            return selection

        print(
            f"Invalid selection. Please enter a number from 1 to "
            f"{len(menu_options)}."
        )


def main():
    csv_file = (
        "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
    )
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    while True:
        selection = display_menu()
        menu_options[selection - 1][1](sales_data)


if __name__ == "__main__":
    main()
