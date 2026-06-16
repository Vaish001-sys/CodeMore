# Task 2 – Error Handling in Python

This is a beginner Python project made for Week 3 of my internship.  
It has two small programs that show how to handle errors using try-except blocks.

---

## What's Inside

| File | What it does |
|---|---|
| `src/division_calculator.py` | Asks for two numbers and divides them |
| `src/list_access.py` | Shows an item from a list based on the index you enter |

---

## How to Run

Make sure Python is installed on your computer.  
Open a terminal in the project folder and run:

**Division Calculator:**
```
python src/division_calculator.py
```

**List Access:**
```
python src/list_access.py
```

No extra libraries needed. Just plain Python.

---

## Sample Output

### division_calculator.py

**Normal run:**
```
========================================
      Simple Division Calculator
========================================
Enter the first number  : 10
Enter the second number : 2

  10.0 ÷ 2.0 = 5.0

✅ Division successful!
========================================
```

**If you type a word instead of a number:**
```
Enter the first number  : hello

❌ Oops! That doesn't look like a valid number.
   Please enter digits only (e.g. 5, 3.14).
========================================
```

**If you divide by zero:**
```
Enter the first number  : 8
Enter the second number : 0

❌ Oops! You cannot divide by zero.
   Please enter a non-zero number as the second number.
========================================
```

---

### list_access.py

**Normal run:**
```
========================================
        List Item Viewer
========================================

Here is our fruit list:
  [0]  Apple
  [1]  Banana
  [2]  Cherry
  [3]  Mango
  [4]  Strawberry

Enter an index number to see the fruit: 2

✅ The fruit at index 2 is: Cherry
========================================
```

**If you type a letter:**
```
Enter an index number to see the fruit: abc

❌ Oops! That is not a valid index.
   Please enter a whole number (e.g. 0, 1, 2, 3, 4).
========================================
```

**If you type a number out of range:**
```
Enter an index number to see the fruit: 9

❌ Oops! That index is out of range.
   Valid indexes are 0 to 4.
========================================
```

---

## What I Learned

- How to use `try` and `except` in Python
- How to handle `ValueError`, `ZeroDivisionError`, and `IndexError`
- How to show friendly error messages to the user
