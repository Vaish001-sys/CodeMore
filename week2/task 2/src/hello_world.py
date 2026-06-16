"""
hello_world.py
--------------
This script demonstrates different data types in Python.
It declares variables, prints their values, and shows their data types.
"""

if __name__ == "__main__":

    # ── String variable ───────────────────────────────────────────────────────
    name = "Alice"                  # A sequence of characters enclosed in quotes

    # ── Integer variable ──────────────────────────────────────────────────────
    age = 20                        # A whole number (no decimal point)

    # ── Float variable ────────────────────────────────────────────────────────
    gpa = 8.75                      # A number with a decimal point

    # ── Boolean variable ──────────────────────────────────────────────────────
    is_student = True               # Can only be True or False


    # ── Print values ──────────────────────────────────────────────────────────
    print("===== Variable Values =====")
    print("Name           :", name)
    print("Age            :", age)
    print("GPA            :", gpa)
    print("Is a student?  :", is_student)

    print()  # blank line for readability

    # ── Print data types ──────────────────────────────────────────────────────
    print("===== Data Types =====")
    print("Type of name        :", type(name))
    print("Type of age         :", type(age))
    print("Type of gpa         :", type(gpa))
    print("Type of is_student  :", type(is_student))
