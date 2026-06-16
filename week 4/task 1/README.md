# Week 4 - Task 1: Modules and Packages

This is a beginner Python project made for my internship.
It shows how to create a custom module, import it, and use a third-party package.

---

## What's Inside

```
task 1/
│
├── src/
│   ├── my_math.py       # custom module with math functions
│   ├── main.py          # imports and uses my_math.py
│   └── package_demo.py  # uses colorama to print colored text
│
├── docs/
│   └── modules_notes.md # my notes on modules and packages
│
├── .gitignore
└── README.md
```

---

## How to Install colorama

colorama is a third-party package that lets you print colored text in the terminal.

Run this command once before running `package_demo.py`:

```
pip install colorama
```

---

## How to Run the Files

Make sure you are inside the `src/` folder first.

**Run main.py:**
```
python main.py
```

**Run package_demo.py:**
```
python package_demo.py
```

> Note: `my_math.py` is a module, not a script. You don't run it directly.

---

## Sample Output

**main.py output:**
```
Addition:      10 + 5 = 15
Subtraction:   10 - 5 = 5
Multiplication: 10 x 5 = 50
```

**package_demo.py output** (colors show in terminal):
```
Success! colorama is working perfectly.
Warning: This is just a demo message.
Error: Something went wrong (just for demo).
Info: colorama makes terminal output colorful and fun!
Bold White: Python third-party packages are easy to use!
```
