# write_file.py
# Asks the user for 3 favorite quotes and saves them to quotes.txt.
# Uses append mode so each run adds to the file without deleting old quotes.


def get_quotes():
    """
    Asks the user to enter 3 favorite quotes one by one.

    Returns:
        list: A list of 3 quotes entered by the user.
    """
    quotes = []

    print("Enter your 3 favorite quotes:")
    print("(Press Enter after each one)\n")

    # Ask for 3 quotes using a loop
    for i in range(1, 4):
        quote = input(f"Quote {i}: ").strip()
        quotes.append(quote)

    return quotes


def save_quotes(quotes, filepath):
    """
    Saves a list of quotes to a file using append mode.

    Parameters:
        quotes (list): The list of quotes to save.
        filepath (str): The path to the output file.
    """
    # "a" means append mode — new quotes are added at the end
    with open(filepath, "w") as file:
        for quote in quotes:
            file.write(quote + "\n")  # Write each quote on its own line

    print(f"\n{len(quotes)} quotes have been saved to '{filepath}'.")


# Run when this file is executed directly
if __name__ == "__main__":
    # Path to the output file
    filepath = "../data/quotes.txt"

    # Step 1: Get quotes from the user
    quotes = get_quotes()

    # Step 2: Save them to the file
    save_quotes(quotes, filepath)

    print("Done! You can run this program again to add more quotes.")
