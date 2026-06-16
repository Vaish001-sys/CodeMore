# read_file.py
# Reads text from data/input.txt and counts the total number of words.


def count_words(filepath):
    """
    Opens a file and counts the total number of words in it.

    Parameters:
        filepath (str): The path to the file to read.

    Returns:
        int: The total word count, or None if the file was not found.
    """
    try:
        # Try to open and read the file
        with open(filepath, "r") as file:
            content = file.read()

        # Split the text into words and count them
        words = content.split()
        total_words = len(words)

        print("File read successfully!")
        print(f"Total word count: {total_words}")

        return total_words

    except FileNotFoundError:
        # This runs if the file does not exist
        print(f"Error: The file '{filepath}' was not found.")
        print("Please make sure 'input.txt' exists inside the 'data' folder.")
        return None


# Run the function when this file is executed directly
if __name__ == "__main__":
    # Path to the input file (relative to the src folder)
    filepath = "../data/input.txt"

    count_words(filepath)
