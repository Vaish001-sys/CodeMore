"""
division_calculator.py

A simple program that asks the user for two numbers
and performs division with basic error handling.
"""


def get_number(prompt):
    """Ask the user to enter a number and return it as a float."""
    number = float(input(prompt))
    return number


def divide(num1, num2):
    """Divide num1 by num2 and return the result."""
    result = num1 / num2
    return result


def main():
    """Main function to run the division calculator."""

    print("=" * 40)
    print("      Simple Division Calculator")
    print("=" * 40)

    try:
        # Ask the user for two numbers
        num1 = get_number("Enter the first number  : ")
        num2 = get_number("Enter the second number : ")

        # Perform the division
        result = divide(num1, num2)

        # Show the result
        print(f"\n  {num1} ÷ {num2} = {result}")
        print("\n✅ Division successful!")

    except ValueError:
        # Triggered when the user types something that is not a number
        print("\n❌ Oops! That doesn't look like a valid number.")
        print("   Please enter digits only (e.g. 5, 3.14).")

    except ZeroDivisionError:
        # Triggered when the second number is zero
        print("\n❌ Oops! You cannot divide by zero.")
        print("   Please enter a non-zero number as the second number.")

    print("=" * 40)


# Run the program
if __name__ == "__main__":
    main()
