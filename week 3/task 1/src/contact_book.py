"""
contact_book.py
---------------
Mini project: A simple contact book using a dictionary.

Features:
- Add a contact (name, phone, email)
- Search for a contact by name
- Display all contacts
- Exit option
"""


# Global dictionary to store contacts
# Format: { "name": {"phone": "...", "email": "..."} }
contacts = {}


def add_contact():
    """Ask the user for details and add a new contact."""
    print("\n--- Add Contact ---")
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty. Please try again.")
        return

    if name.lower() in (k.lower() for k in contacts):
        print(f"A contact named '{name}' already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    # Store contact in the dictionary
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Contact '{name}' added successfully!")


def search_contact():
    """Search for a contact by name and display their details."""
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ").strip()

    # Case-insensitive search
    for key in contacts:
        if key.lower() == name.lower():
            print(f"\nContact Found:")
            print(f"  Name  : {key}")
            print(f"  Phone : {contacts[key]['phone']}")
            print(f"  Email : {contacts[key]['email']}")
            return

    print(f"No contact found with name '{name}'.")


def delete_contact():
    """Delete an existing contact by name."""
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ").strip()

    # Case-insensitive search for the contact to delete
    for key in contacts:
        if key.lower() == name.lower():
            del contacts[key]
            print(f"Contact '{key}' deleted successfully!")
            return

    print(f"No contact found with name '{name}'.")


def display_all_contacts():
    """Display all contacts stored in the contact book."""
    print("\n--- All Contacts ---")

    if not contacts:
        print("Your contact book is empty.")
        return

    print(f"{'No.':<5} {'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 60)

    for i, (name, details) in enumerate(contacts.items(), start=1):
        print(f"{i:<5} {name:<20} {details['phone']:<15} {details['email']}")


def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 35)
    print("        CONTACT BOOK MENU")
    print("=" * 35)
    print("  1. Add Contact")
    print("  2. Search Contact")
    print("  3. Display All Contacts")
    print("  4. Delete Contact")
    print("  5. Exit")
    print("=" * 35)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    """Main function to run the contact book application."""
    print("\nWelcome to the Contact Book!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_all_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\nGoodbye! Your contacts will not be saved after exit.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
