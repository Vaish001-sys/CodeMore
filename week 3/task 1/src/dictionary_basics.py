"""
dictionary_basics.py
---------------------
Demonstrates basic dictionary operations in Python:
- Creating a dictionary
- Adding items
- Updating items
- Iterating through a dictionary
- Printing key-value pairs
"""


def create_dictionary():
    """Create and return a sample dictionary with student information."""
    student = {
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "subject": "Python"
    }
    return student


def add_items(student):
    """Add new key-value pairs to the dictionary."""
    student["email"] = "alice@example.com"
    student["city"] = "Mumbai"
    print("Added 'email' and 'city' to the dictionary.")
    return student


def update_items(student):
    """Update existing values in the dictionary."""
    student["age"] = 21          # Update age
    student["grade"] = "A+"      # Update grade
    print("Updated 'age' and 'grade' in the dictionary.")
    return student


def iterate_dictionary(student):
    """Iterate through the dictionary and print key-value pairs."""
    print("\n--- All Key-Value Pairs ---")
    for key, value in student.items():
        print(f"  {key}: {value}")


def print_keys_and_values(student):
    """Print keys and values separately."""
    print("\n--- Keys ---")
    for key in student.keys():
        print(f"  {key}")

    print("\n--- Values ---")
    for value in student.values():
        print(f"  {value}")


def get_student_input():
    """Ask the user to enter a student name and marks, then display the result."""
    print("\n--- Enter Your Student Info ---")
    name = input("Enter student name: ").strip()
    marks = input("Enter student marks (out of 100): ").strip()

    # Store the input in a new dictionary
    student_info = {
        "name": name,
        "marks": marks
    }

    # Display the stored result
    print("\n--- Stored Result ---")
    for key, value in student_info.items():
        print(f"  {key}: {value}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 40)
    print("       DICTIONARY BASICS DEMO")
    print("=" * 40)

    # Step 1: Create
    print("\n[1] Creating dictionary...")
    student = create_dictionary()
    print(f"    Dictionary created: {student}")

    # Step 2: Add items
    print("\n[2] Adding items...")
    student = add_items(student)

    # Step 3: Update items
    print("\n[3] Updating items...")
    student = update_items(student)

    # Step 4: Iterate and print key-value pairs
    print("\n[4] Iterating through dictionary...")
    iterate_dictionary(student)

    # Step 5: Print keys and values separately
    print("\n[5] Printing keys and values separately...")
    print_keys_and_values(student)

    # Step 6: Interactive input from the user
    print("\n[6] Now it's your turn — enter your own student data!")
    get_student_input()

    print("\n" + "=" * 40)
    print("          DEMO COMPLETE")
    print("=" * 40)


if __name__ == "__main__":
    main()
