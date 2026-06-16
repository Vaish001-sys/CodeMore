"""
debugged_script.py
------------------
This file shows a simple buggy program and its corrected version.

Each bug is clearly marked with:
  - ORIGINAL ERROR  : what the bug was
  - FIX APPLIED     : what was changed to fix it

This is meant to help beginners understand common Python mistakes.
"""

# ─────────────────────────────────────────────
#  SECTION 1 — Buggy Version (shown as comments)
# ─────────────────────────────────────────────
#
# The program below was supposed to:
#   1. Store a list of student names
#   2. Print a greeting for each student
#   3. Count and print how many students there are
#   4. Find and print the first student alphabetically
#
# But it had FOUR bugs. Each bug is described below.
#
# -----------------------------------------------
# BUG 1 — Wrong variable name (NameError)
# -----------------------------------------------
# ORIGINAL ERROR : 'studens' was a typo; Python could not find that variable.
# ORIGINAL CODE  : for name in studens:
#
# -----------------------------------------------
# BUG 2 — String used instead of integer for count (TypeError)
# -----------------------------------------------
# ORIGINAL ERROR : count was set to "0" (a string), so adding 1 to it failed.
# ORIGINAL CODE  : count = "0"
#
# -----------------------------------------------
# BUG 3 — Wrong built-in function used (TypeError)
# -----------------------------------------------
# ORIGINAL ERROR : len() does not sort; min() should have been used instead.
# ORIGINAL CODE  : first_alphabetically = len(students)
#
# -----------------------------------------------
# BUG 4 — Missing colon on function definition (SyntaxError)
# -----------------------------------------------
# ORIGINAL ERROR : Python requires a colon (:) at the end of a def line.
# ORIGINAL CODE  : def greet_student(name)
#
# ─────────────────────────────────────────────
#  SECTION 2 — Fixed Version (actual running code)
# ─────────────────────────────────────────────


def greet_student(name):          # FIX 4: Added the missing colon ':'
    """
    Print a simple greeting for a student.

    Args:
        name (str): The student's name.
    """
    print(f"Hello, {name}! Welcome to the class.")


def main():
    """
    Main function — runs the corrected student list program.
    """

    # A list of student names
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    print("=" * 40)
    print("        Student Greeting Program")
    print("=" * 40)

    # ── Greet every student in the list ──────
    for name in students:         # FIX 1: Corrected 'studens' → 'students'
        greet_student(name)

    print()  # blank line for readability

    # ── Count the students ───────────────────
    count = 0                     # FIX 2: Changed "0" (string) → 0 (integer)
    for _ in students:
        count = count + 1

    print(f"Total students : {count}")

    # ── Find the first name alphabetically ───
    first_alphabetically = min(students)   # FIX 3: Changed len() → min()
    print(f"First name (A-Z): {first_alphabetically}")

    print("=" * 40)
    print("Program finished successfully!")


# Run main() only when this script is executed directly
if __name__ == "__main__":
    main()
