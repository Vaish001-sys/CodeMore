def check_even_or_odd(number):
    """Check whether the given number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")


def check_sign(number):
    """Check whether the given number is positive, negative, or zero."""
    if number > 0:
        print(f"{number} is a Positive number.")
    elif number < 0:
        print(f"{number} is a Negative number.")
    else:
        print(f"{number} is Zero.")


def main():
    # Accept integer input from the user
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    print()  # Blank line for readability

    # --- Even / Odd Check ---
    check_even_or_odd(number)

    # --- Positive / Negative / Zero Check ---
    check_sign(number)

    
if __name__ == "__main__":
    main()
