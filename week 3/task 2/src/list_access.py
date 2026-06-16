"""
list_access.py

A simple program that holds a list of 5 fruits,
asks the user for an index, and displays the item
at that position with basic error handling.
"""


def get_index(prompt):
    """Ask the user to enter an index and return it as an integer."""
    index = int(input(prompt))
    return index


def get_item(my_list, index):
    """Return the item at the given index from my_list."""
    item = my_list[index]
    return item


def main():
    """Main function to run the list access program."""

    # A fixed list of 5 fruits
    fruits = ["Apple", "Banana", "Cherry", "Mango", "Strawberry"]

    print("=" * 40)
    print("        List Item Viewer")
    print("=" * 40)

    # Show the user what is in the list
    print("\nHere is our fruit list:")
    for i, fruit in enumerate(fruits):
        print(f"  [{i}]  {fruit}")

    print()  # blank line for readability

    try:
        # Ask the user for an index
        index = get_index("Enter an index number to see the fruit: ")

        # Reject negative indexes and indexes above 4
        if index < 0 or index > 4:
            print(f"\n❌ Oops! That index is out of range.")
            print(f"   Valid indexes are 0 to {len(fruits) - 1}.")
        else:
            # Fetch the item at that index
            item = get_item(fruits, index)

            # Display the result
            print(f"\n✅ The fruit at index {index} is: {item}")


    except ValueError:
        # Triggered when the user types something that is not a whole number
        print("\n❌ Oops! That is not a valid index.")
        print("   Please enter a whole number (e.g. 0, 1, 2, 3, 4).")

    except IndexError:
        # Triggered when the index is outside the range of the list
        print("\n❌ Oops! That index is out of range.")
        print(f"   Valid indexes are 0 to {len(fruits) - 1}.")

    print("=" * 40)


# Run the program
if __name__ == "__main__":
    main()
