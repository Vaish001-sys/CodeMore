# Code Explanation

This document explains how the code works in simple terms.

---

## utils.py

This file contains all the helper functions.
It also stores the list called `items` which holds all the data.

---

### `add_item(item)`

- Takes a word or phrase as input.
- Strips extra spaces from it.
- If the input is empty, it returns an error message.
- Otherwise, it adds the item to the `items` list and returns a success message.

---

### `remove_item(item)`

- Takes a word or phrase as input.
- First checks if the list is empty — if yes, returns a message saying nothing to remove.
- If the item exists in the list, it removes it and returns a success message.
- If the item is not found, it returns a not found message.

---

### `search_item(item)`

- Takes a word or phrase as input.
- First checks if the list is empty — if yes, returns a message saying nothing to search.
- If the item is found, it returns the position (starting from 1, not 0).
- If the item is not found, it returns a not found message.

---

### `display_items()`

- Takes no input.
- If the list is empty, it returns a message saying the list is empty.
- Otherwise, it loops through the list and returns all items with their position numbers.

---

## main.py

This file runs the program.

- It imports `utils.py` to use the helper functions.
- It has a `show_menu()` function that prints the menu each time.
- It has a `main()` function that runs a loop using `while True`.
- Inside the loop, it asks the user to enter a number (1 to 5).
- Based on the number, it calls the right function from `utils.py`.
- If the user enters 5, the loop breaks and the program ends.
- If the user enters anything else, it shows an error message.

---

## How the List Works

- The list `items` is defined in `utils.py` as an empty list: `items = []`
- All functions in `utils.py` use this same list.
- The list only exists while the program is running. When you close it, the data is gone.
