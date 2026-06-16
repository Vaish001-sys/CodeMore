# Simple Calculator

A beginner Python project that works as a basic calculator.
It runs in the terminal and lets you do simple math operations.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Exit option
- Handles wrong menu input
- Handles division by zero

---

## How to Run

Make sure Python is installed on your computer.

Open a terminal and go to the project folder:

```
cd "week 4/task 2"
```

Run the calculator:

```
python src/calculator.py
```

That's it! The menu will show up and you can start using it.

---

## Sample Output

```
Welcome to the Simple Calculator!

===================================
        SIMPLE CALCULATOR
===================================
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Exit
===================================
  Select an option (1-5): 1
  Enter first number  : 10
  Enter second number : 5

  Result: 10 + 5 = 15

===================================
        SIMPLE CALCULATOR
===================================
  ...
  Select an option (1-5): 4
  Enter first number  : 8
  Enter second number : 0

  [!] Error: Cannot divide by zero!

===================================
  ...
  Select an option (1-5): 6

  [!] Invalid choice. Please enter a number between 1 and 5.

===================================
  ...
  Select an option (1-5): 5

  Goodbye! Thanks for using the calculator.
```

---

## Project Structure

```
task 2/
│
├── src/
│   └── calculator.py   # main calculator file
│
├── docs/
│   └── project_explanation.md  # how the project works
│
└── README.md           # this file
```

---

## Requirements

- Python 3.x
- No extra libraries needed
