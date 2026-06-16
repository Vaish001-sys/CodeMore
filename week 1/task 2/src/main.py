# main.py
# Entry point of the program.
# Provides an interactive CLI menu for managing a list of items.

import utils  # Import our helper functions from utils.py


def show_menu():
    """Displays the main menu options to the user."""
    print("\n=============================")
    print("      ITEM MANAGER MENU      ")
    print("=============================")
    print("  1. Add Item")
    print("  2. View Items")
    print("  3. Search Item")
    print("  4. Remove Item")
    print("  5. Exit")
    print("=============================")


def main():
    """Main function that runs the interactive menu loop."""
    print("Welcome to the Item Manager!")

    while True:
        show_menu()

        # Get user's choice
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # --- Add Item ---
            item = input("Enter the item to add: ")
            message = utils.add_item(item)
            print(message)

        elif choice == "2":
            # --- View Items ---
            print(utils.display_items())

        elif choice == "3":
            # --- Search Item ---
            item = input("Enter the item to search: ")
            message = utils.search_item(item)
            print(message)

        elif choice == "4":
            # --- Remove Item ---
            item = input("Enter the item to remove: ")
            message = utils.remove_item(item)
            print(message)

        elif choice == "5":
            # --- Exit ---
            print("Goodbye! Thanks for using Item Manager.")
            break  # Exit the loop and end the program

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
