# Task 3 — Error Handling and Debugging in Python

This is a beginner Python project made as part of my internship (Week 4, Task 3).

The goal was to learn how to handle errors properly in Python
and to practice finding and fixing bugs in a script.

---

## What's Inside

| File | What it does |
|------|--------------|
| `src/error_handling_demo.py` | Asks for two numbers and divides them. Handles common errors. |
| `src/debugged_script.py` | Shows a buggy program and explains how each bug was fixed. |
| `docs/debugging_notes.md` | My notes explaining try, except, errors, and debugging. |

---

## How to Run

Make sure Python is installed on your computer.
You can check by opening a terminal and typing:

```
python --version
```

### Run the error handling demo

```
python src/error_handling_demo.py
```

### Run the debugged script

```
python src/debugged_script.py
```

No extra libraries needed. Just plain Python.

---

## Sample Output

### error_handling_demo.py — normal run

```
========================================
   Simple Division Calculator
========================================
Enter the first number  : 10
Enter the second number : 2

Result: 10.0 ÷ 2.0 = 5.0
Division completed successfully!
========================================
```

### error_handling_demo.py — divide by zero

```
========================================
   Simple Division Calculator
========================================
Enter the first number  : 10
Enter the second number : 0
Oops! You can't divide by zero. Please choose a different second number.
========================================
```

### error_handling_demo.py — invalid input

```
========================================
   Simple Division Calculator
========================================
Enter the first number  : hello
Oops! That doesn't look like a valid number. Please enter digits only.
Program stopped due to invalid input.
========================================
```

### debugged_script.py

```
========================================
        Student Greeting Program
========================================
Hello, Alice! Welcome to the class.
Hello, Bob! Welcome to the class.
Hello, Charlie! Welcome to the class.
Hello, Diana! Welcome to the class.
Hello, Eve! Welcome to the class.

Total students : 5
First name (A-Z): Alice
========================================
Program finished successfully!
```

---

## What I Learned

- How to use `try` and `except` to catch errors
- The difference between `ValueError` and `ZeroDivisionError`
- How to read error messages and find bugs in code
- How to write simple, clean Python programs

---

*Made by an intern. Week 4, Task 3.*
