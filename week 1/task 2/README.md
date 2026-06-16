# Item Manager

A simple Python CLI program to manage a list of items.
This was made as part of my internship task.

---

## What It Does

- Add items to a list
- View all items
- Search for an item
- Remove an item

---

## Files

```
task 2/
├── src/
│   ├── main.py       # runs the program
│   └── utils.py      # helper functions
├── tests/
│   └── test_utils.py # basic tests
├── docs/
│   └── explanation.md
├── README.md
└── .gitignore
```

---

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal and go to the `src` folder:

```
cd src
```

3. Run the program:

```
python main.py
```

---

## Menu Options

```
1. Add Item
2. View Items
3. Search Item
4. Remove Item
5. Exit
```

---

## How to Run Tests

Go to the `task 2` folder and run:

```
python -m pytest tests/
```

Or without pytest:

```
python tests/test_utils.py
```

---

## Requirements

- Python 3.x
- No external libraries needed
