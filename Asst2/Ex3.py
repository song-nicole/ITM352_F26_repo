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
            "\n \nHow many initial rows would you like to see? Please enter a whole number or 'all' for all rows."
        ).strip().lower()

        if num_rows == 'all':
            num_rows = len(data)
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

#Main loop
def main():
    csv_file = (
        "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
    )
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    while True:
        display_initial_rows(sales_data)


if __name__ == "__main__":
    main()
