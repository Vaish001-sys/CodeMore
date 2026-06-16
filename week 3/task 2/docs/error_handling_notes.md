# Error Handling Notes

These are my personal notes on error handling in Python.  
Written in simple words so I can understand it later.

---

## What is an Error?

When Python runs your code and something goes wrong, it stops and shows an error message.  
This is called an **exception** or a **runtime error**.

If we don't handle it, the whole program crashes.  
We use `try` and `except` to stop that from happening.

---

## try

`try` is a block where you put code that *might* go wrong.  
Python will **try** to run it. If something breaks, it jumps to `except`.

```python
try:
    number = int(input("Enter a number: "))
```

Think of it like saying:  
*"Hey Python, try this. If it fails, don't crash — just go to the except part."*

---

## except

`except` is where you write what should happen if the `try` block fails.  
You can have more than one `except` for different types of errors.

```python
except ValueError:
    print("That was not a number!")
```

Think of it like a safety net.  
If `try` falls, `except` catches it.

---

## ValueError

A `ValueError` happens when you give Python the **right type** of thing,  
but the **wrong value** inside it.

**Example:**  
You call `int()` and pass it the word `"hello"`.  
Python knows you want a number, but `"hello"` can't be turned into one.  
So it raises a `ValueError`.

```python
try:
    number = int("hello")   # this will fail
except ValueError:
    print("Oops! That is not a valid number.")
```

**When does it happen in our project?**  
In `division_calculator.py` — if you type `abc` instead of a number.  
In `list_access.py` — if you type `abc` instead of an index.

---

## ZeroDivisionError

A `ZeroDivisionError` happens when you try to **divide any number by zero**.  
This is not allowed in math and Python agrees.

```python
try:
    result = 10 / 0   # this will fail
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

**When does it happen in our project?**  
In `division_calculator.py` — if you enter `0` as the second number.

---

## IndexError

A list in Python has positions called **indexes**, starting from `0`.  
An `IndexError` happens when you try to access an index that **does not exist** in the list.

```python
fruits = ["Apple", "Banana", "Cherry"]  # indexes 0, 1, 2

try:
    print(fruits[10])   # index 10 does not exist
except IndexError:
    print("That index is out of range!")
```

**When does it happen in our project?**  
In `list_access.py` — if you type a number like `9` that is outside the list.

> **Note:** Python also allows negative indexes like `-1` (which means the last item).  
> In our project, we added an extra check to block negative numbers on purpose.

---

## Quick Summary

| Keyword | What it does |
|---|---|
| `try` | Runs code that might fail |
| `except` | Runs if the `try` block fails |
| `ValueError` | Wrong value given (e.g. text where a number is expected) |
| `ZeroDivisionError` | Tried to divide by zero |
| `IndexError` | Tried to access a list position that doesn't exist |
