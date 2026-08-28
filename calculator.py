"""
Simple Calculator Program
Performs basic math operations with error handling
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers with error handling"""
    if y == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return x / y


def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True:
        try:
            # Get user input for two numbers
            print("\nEnter two numbers to perform a calculation")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Display operation choices
            print("\nSelect operation:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Exit")
            
            choice = input("\nEnter choice (1/2/3/4/5): ").strip()
            
            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            elif choice == '5':
                print("\nThank you for using the calculator. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select 1, 2, 3, 4, or 5.")
                
        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
