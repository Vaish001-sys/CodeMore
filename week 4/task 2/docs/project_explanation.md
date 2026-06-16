# Project Explanation — Simple Calculator

This document explains how the Simple Calculator works.
It's written in simple language so anyone can understand it.

---

## 1. The Calculator Menu

When you run the program, a menu appears on the screen like this:

```
===================================
        SIMPLE CALCULATOR
===================================
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Exit
===================================
  Select an option (1-5):
```

You just type a number from 1 to 5 and press Enter.

- If you type **1**, it will ask for two numbers and add them.
- If you type **2**, it will subtract them.
- If you type **3**, it will multiply them.
- If you type **4**, it will divide them.
- If you type **5**, the program will close.

The menu keeps showing again and again after each calculation,
so you can do as many calculations as you want without restarting.

If you type something that is not 1, 2, 3, 4, or 5 — the program
will show an error message and ask you again. It won't crash.

---

## 2. Arithmetic Operations

Each operation is a separate function in the code.

### Addition
```python
def add(a, b):
    return a + b
```
Takes two numbers and returns their sum.
Example: `add(3, 4)` gives `7`

---

### Subtraction
```python
def subtract(a, b):
    return a - b
```
Takes two numbers and returns the first minus the second.
Example: `subtract(10, 3)` gives `7`

---

### Multiplication
```python
def multiply(a, b):
    return a * b
```
Takes two numbers and returns their product.
Example: `multiply(4, 5)` gives `20`

---

### Division
```python
def divide(a, b):
    if b == 0:
        return None
    return a / b
```
Takes two numbers and returns the first divided by the second.
Example: `divide(10, 2)` gives `5.0`

The special case here is when `b` is 0 — we handle that separately.
(explained in the next section)

---

## 3. Division by Zero Handling

In math, dividing any number by zero is not allowed.
If you try to do `10 / 0` in Python without handling it,
the program will crash with an error called `ZeroDivisionError`.

To avoid that, the `divide()` function checks if the second
number is zero **before** doing the division:

```python
if b == 0:
    return None   # return nothing instead of crashing
```

Then in the main part of the program, we check if the result
came back as `None`:

```python
if result is None:
    print("[!] Error: Cannot divide by zero!")
    continue   # go back to the menu
```

So instead of crashing, the program shows a friendly message
and goes back to the menu. The user can try again.

---

## Summary

| Part | What it does |
|---|---|
| Menu | Shows options and reads user input |
| add / subtract / multiply / divide | Do the actual math |
| Division by zero check | Stops the program from crashing |
| Input validation | Handles wrong menu choices and non-number inputs |

The whole program is in one file: `src/calculator.py`
No extra files or libraries are needed.
