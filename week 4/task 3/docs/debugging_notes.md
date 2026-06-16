# Debugging Notes — What I Learned

These are my personal notes from Week 4, Task 3 of the internship.
I'm writing this in simple language so I can look back and understand it later.

---

## 1. What is `try`?

`try` is a block of code that Python will *attempt* to run.

Think of it like saying:
> "Hey Python, *try* to do this... but if something goes wrong, don't crash."

**Example:**

```python
try:
    number = int(input("Enter a number: "))
```

Python will try to convert what the user typed into a number.
If the user types something like "abc", it won't work — but `try` gives us
a chance to deal with that instead of crashing.

---

## 2. What is `except`?

`except` is the block that runs *only if* something went wrong inside `try`.

Think of it like:
> "IF the try block failed, then do THIS instead."

**Example:**

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

If the user types "hello", Python jumps to `except` and shows the message
instead of crashing with a red error.

---

## 3. What is `ValueError`?

A `ValueError` happens when you give Python the *right type* of thing,
but the *wrong value* inside it.

**Common example:**

```python
int("hello")   # Python expects digits, not letters
```

This causes:
```
ValueError: invalid literal for int() with base 10: 'hello'
```

In our program, this happens when the user types letters instead of a number.

---

## 4. What is `ZeroDivisionError`?

A `ZeroDivisionError` happens when you try to divide any number by zero.

In maths, dividing by zero is impossible (undefined).
Python follows the same rule and throws this error.

**Example:**

```python
result = 10 / 0
```

This causes:
```
ZeroDivisionError: division by zero
```

In our program, this happens if the user enters `0` as the second number.

---

## 5. What is Debugging?

Debugging means finding and fixing mistakes (called "bugs") in your code.

The word "bug" in programming comes from a real story — a moth once got
stuck inside an early computer and caused it to malfunction. 🦗

### How I debug:

1. **Read the error message** — Python tells you the line number and what went wrong
2. **Find that line** in your code
3. **Think about why** that line could fail
4. **Fix it** and run again
5. **Repeat** until it works

---

## 6. Fixing Errors — What I Did in `debugged_script.py`

Here are the four bugs I fixed and what I learned from each one:

---

### Bug 1 — Typo in variable name (`NameError`)

**What went wrong:**
```python
for name in studens:   # 'studens' doesn't exist
```

**What I fixed:**
```python
for name in students:  # correct spelling
```

**Lesson:** Python is case-sensitive and spelling-sensitive.
If a variable name is wrong by even one letter, Python can't find it.

---

### Bug 2 — Wrong data type (`TypeError`)

**What went wrong:**
```python
count = "0"        # "0" is a string, not a number
count = count + 1  # can't add a number to a string!
```

**What I fixed:**
```python
count = 0          # 0 without quotes is an integer
count = count + 1  # now this works fine
```

**Lesson:** `"0"` and `0` look similar but are very different in Python.
One is text, the other is a number.

---

### Bug 3 — Wrong built-in function (`TypeError` / wrong result)

**What went wrong:**
```python
first_alphabetically = len(students)   # len() gives a count, not a name
```

**What I fixed:**
```python
first_alphabetically = min(students)   # min() gives the smallest/first item
```

**Lesson:** Using the wrong function gives you either an error or
a completely wrong answer. Always check what a function actually returns.

---

### Bug 4 — Missing colon (`SyntaxError`)

**What went wrong:**
```python
def greet_student(name)    # missing colon at the end
```

**What I fixed:**
```python
def greet_student(name):   # colon added
```

**Lesson:** Python uses colons to start blocks like functions, loops, and if-statements.
Forgetting one is one of the most common beginner mistakes.

---

## Quick Reference Table

| Error | When it happens | Example |
|-------|----------------|---------|
| `ValueError` | Right type, wrong value | `int("hello")` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `NameError` | Variable name not found | Typo in variable name |
| `TypeError` | Wrong type used | Adding string + integer |
| `SyntaxError` | Code is written incorrectly | Missing `:` after `def` |

---

*These notes were written during Week 4 of my internship. Written in simple words on purpose.*
