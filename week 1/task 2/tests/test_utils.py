# test_utils.py
# Basic tests for the functions in utils.py.
# These tests check that each function works correctly.

import sys
import os

# This line lets Python find utils.py inside the src folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import utils


# ---- Helper: Reset the list before each test ----

def reset():
    """Clears the items list so each test starts fresh."""
    utils.items.clear()


# ---- Tests for add_item ----

def test_add_item_normal():
    """Adding a normal item should work."""
    reset()
    result = utils.add_item("Apple")
    assert "added" in result
    assert "Apple" in utils.items

def test_add_item_empty_string():
    """Adding an empty string should not add anything."""
    reset()
    result = utils.add_item("   ")
    assert "empty" in result.lower()
    assert len(utils.items) == 0


# ---- Tests for remove_item ----

def test_remove_item_exists():
    """Removing an item that is in the list should work."""
    reset()
    utils.items.append("Banana")
    result = utils.remove_item("Banana")
    assert "removed" in result
    assert "Banana" not in utils.items

def test_remove_item_not_found():
    """Removing an item that does not exist should say not found."""
    reset()
    utils.items.append("Banana")
    result = utils.remove_item("Mango")
    assert "not found" in result.lower()

def test_remove_item_empty_list():
    """Removing from an empty list should say list is empty."""
    reset()
    result = utils.remove_item("Anything")
    assert "empty" in result.lower()


# ---- Tests for search_item ----

def test_search_item_found():
    """Searching for an item that exists should return its position."""
    reset()
    utils.items.append("Cherry")
    result = utils.search_item("Cherry")
    assert "found" in result.lower()

def test_search_item_not_found():
    """Searching for an item not in the list should say not found."""
    reset()
    utils.items.append("Cherry")
    result = utils.search_item("Grapes")
    assert "not found" in result.lower()

def test_search_item_empty_list():
    """Searching in an empty list should say list is empty."""
    reset()
    result = utils.search_item("Cherry")
    assert "empty" in result.lower()


# ---- Tests for display_items ----

def test_display_items_with_items():
    """Display should return a list when items exist."""
    reset()
    utils.items.append("Dog")
    utils.items.append("Cat")
    result = utils.display_items()
    assert "Dog" in result
    assert "Cat" in result

def test_display_items_empty_list():
    """Display should return an empty message when list is empty."""
    reset()
    result = utils.display_items()
    assert "empty" in result.lower()


# ---- Run all tests manually (without pytest) ----

if __name__ == "__main__":
    tests = [
        test_add_item_normal,
        test_add_item_empty_string,
        test_remove_item_exists,
        test_remove_item_not_found,
        test_remove_item_empty_list,
        test_search_item_found,
        test_search_item_not_found,
        test_search_item_empty_list,
        test_display_items_with_items,
        test_display_items_empty_list,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"  PASS: {test.__name__}")
            passed += 1
        except AssertionError:
            print(f"  FAIL: {test.__name__}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed out of {len(tests)} tests.")
