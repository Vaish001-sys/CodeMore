"""
main.py
-------
Demonstrates how to import and use functions
from a custom module (my_math.py).
"""

# Import all three functions from our custom module
from my_math import add, subtract, multiply

if __name__ == "__main__":
    # --- Using the add() function ---
    result_add = add(10, 5)
    print("Addition:      10 + 5 =", result_add)

    # --- Using the subtract() function ---
    result_sub = subtract(10, 5)
    print("Subtraction:   10 - 5 =", result_sub)

    # --- Using the multiply() function ---
    result_mul = multiply(10, 5)
    print("Multiplication: 10 x 5 =", result_mul)
