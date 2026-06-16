# ============================================================
# Simple Calculator
# A beginner-level menu-driven calculator program.
# Supports: Addition, Subtraction, Multiplication, Division
# ============================================================


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """
    Return the quotient of a divided by b.
    Returns None if b is zero (division by zero).
    """
    if b == 0:
        return None  # Cannot divide by zero
    return a / b


def get_numbers():
    """
    Prompt the user to enter two numbers.
    Keeps asking until valid numbers are entered.
    Returns a tuple (num1, num2).
    """
    while True:
        try:
            num1 = float(input("  Enter first number  : "))
            num2 = float(input("  Enter second number : "))
            return num1, num2
        except ValueError:
            print("  [!] Invalid input. Please enter numeric values.\n")


def show_menu():
    """Print the calculator menu."""
    print()
    print("=" * 35)
    print("        SIMPLE CALCULATOR")
    print("=" * 35)
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Exit")
    print("=" * 35)


def main():
    """
    Main function — runs the calculator loop.
    Displays the menu, reads the user's choice,
    performs the selected operation, and shows the result.
    """
    print("\nWelcome to the Simple Calculator!")

    while True:
        show_menu()

        choice = input("  Select an option (1-5): ").strip()

        # --- Exit ---
        if choice == "5":
            print("\n  Goodbye! Thanks for using the calculator.\n")
            break

        # --- Validate menu choice ---
        if choice not in ("1", "2", "3", "4"):
            print("\n  [!] Invalid choice. Please enter a number between 1 and 5.")
            continue

        # --- Get input numbers ---
        num1, num2 = get_numbers()

        # --- Perform operation ---
        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"

            # Handle division by zero
            if result is None:
                print("\n  [!] Error: Cannot divide by zero!")
                continue

        # --- Display result ---
        # Format: remove unnecessary .0 for whole numbers
        n1 = int(num1) if num1 == int(num1) else num1
        n2 = int(num2) if num2 == int(num2) else num2
        res = int(result) if result == int(result) else round(result, 6)

        print(f"\n  Result: {n1} {operator} {n2} = {res}")


# --- Entry point ---
if __name__ == "__main__":
    main()
