"""
error_handling_demo.py
----------------------
A beginner-friendly program that demonstrates error handling in Python.

It asks the user for two numbers and divides them.
It handles two common errors:
  1. ValueError   - when the user types something that isn't a number
  2. ZeroDivisionError - when the user tries to divide by zero
"""


def get_number(prompt):
    """
    Ask the user to enter a number.
    If they type something invalid, show a friendly message and return None.
    """
    try:
        # Try to convert whatever the user typed into a float
        number = float(input(prompt))
        return number

    except ValueError:
        # This runs if the user typed letters or symbols instead of a number
        print("Oops! That doesn't look like a valid number. Please enter digits only.")
        return None


def divide(numerator, denominator):
    """
    Divide two numbers and return the result.
    If the denominator is zero, show a friendly message and return None.
    """
    try:
        result = numerator / denominator
        return result

    except ZeroDivisionError:
        # This runs if the user entered 0 as the second number
        print("Oops! You can't divide by zero. Please choose a different second number.")
        return None


def main():
    """
    Main function — runs the division program step by step.
    """
    print("=" * 40)
    print("   Simple Division Calculator")
    print("=" * 40)

    # Step 1: Get the first number from the user
    num1 = get_number("Enter the first number  : ")

    # If get_number returned None, we stop here
    if num1 is None:
        print("Program stopped due to invalid input.")
        return

    # Step 2: Get the second number from the user
    num2 = get_number("Enter the second number : ")

    # If get_number returned None, we stop here
    if num2 is None:
        print("Program stopped due to invalid input.")
        return

    # Step 3: Try to divide the two numbers
    result = divide(num1, num2)

    # Step 4: Display the result if division was successful
    if result is not None:
        print(f"\nResult: {num1} ÷ {num2} = {result}")
        print("Division completed successfully!")

    print("=" * 40)


# This makes sure main() only runs when we execute THIS file directly,
# not when it is imported by another file.
if __name__ == "__main__":
    main()
