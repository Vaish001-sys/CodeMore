# utils.py
# Contains helper functions for managing the item list.

# The main list that stores all items
items = []


def add_item(item):
    """
    Adds a new item to the list.
    
    Parameters:
        item (str): The item to add.
    
    Returns:
        str: A confirmation message.
    """
    item = item.strip()  # Remove extra spaces

    if not item:
        return "Item name cannot be empty."

    items.append(item)
    return f"'{item}' has been added to the list."


def remove_item(item):
    """
    Removes an item from the list if it exists.
    
    Parameters:
        item (str): The item to remove.
    
    Returns:
        str: A confirmation or error message.
    """
    item = item.strip()

    if not items:
        return "The list is empty. Nothing to remove."

    if item in items:
        items.remove(item)
        return f"'{item}' has been removed from the list."
    else:
        return f"'{item}' was not found in the list."


def search_item(item):
    """
    Searches for an item in the list.
    
    Parameters:
        item (str): The item to search for.
    
    Returns:
        str: A message saying whether the item was found or not.
    """
    item = item.strip()

    if not items:
        return "The list is empty. Nothing to search."

    if item in items:
        index = items.index(item)
        return f"'{item}' was found at position {index + 1}."
    else:
        return f"'{item}' was not found in the list."


def display_items():
    """
    Displays all items currently in the list.
    
    Returns:
        str: A formatted list of items or a message if the list is empty.
    """
    if not items:
        return "The list is empty. Add some items first!"

    result = "\n--- Current Items ---\n"
    for index, item in enumerate(items, start=1):
        result += f"  {index}. {item}\n"
    result += "---------------------"
    return result
