# ============================================================
# File: loop_operations.py
# Description: Demonstrates loop-based operations:
#              1. Multiplication table for a user-given number
#              2. Sum of first N natural numbers
#              3. Right-angled star pattern of N rows
# ============================================================


def multiplication_table(n):
    """Print the multiplication table for the given number n (up to 10)."""
    print(f"\n--- Multiplication Table for {n} ---")
    for i in range(1, 11):          # Loop from 1 to 10
        print(f"{n} x {i:2} = {n * i}")


def sum_of_natural_numbers(n):
    """Calculate and print the sum of the first N natural numbers."""
    total = 0
    for i in range(1, n + 1):       # Add each number from 1 to N
        total += i
    print(f"\n--- Sum of First {n} Natural Numbers ---")
    print(f"Sum = {total}")
    # Formula verification (optional): n*(n+1)//2
    print(f"(Formula check: {n} × ({n}+1) / 2 = {n * (n + 1) // 2})")


def star_pattern(n):
    """Print a right-angled star pattern with N rows."""
    print(f"\n--- Right-Angled Star Pattern ({n} rows) ---")
    for i in range(1, n + 1):       # Outer loop controls the number of rows
        print("* " * i)             # Inner stars increase by 1 each row


def main():
    # --------------------------------------------------------
    # 1. Multiplication Table
    # --------------------------------------------------------
    try:
        num = int(input("Enter a number for multiplication table: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    multiplication_table(num)

    # --------------------------------------------------------
    # 2. Sum of First N Natural Numbers
    # --------------------------------------------------------
    try:
        n = int(input("\nEnter N to calculate sum of first N natural numbers: "))
        if n < 1:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    sum_of_natural_numbers(n)

    # --------------------------------------------------------
    # 3. Right-Angled Star Pattern
    # --------------------------------------------------------
    try:
        rows = int(input("\nEnter number of rows for star pattern: "))
        if rows < 1:
            print("Rows must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    star_pattern(rows)


# Entry point
if __name__ == "__main__":
    main()
