# My Notes: Modules and Packages

These are my personal notes from Week 4 of my internship.
Written in simple words so I can look back and understand quickly.

---

## What is a Module?

A module is just a Python file.

That's it. If you have a file called `my_math.py`, that file is a module.
You can put functions inside it and use them in other files.

Think of it like a toolbox. You put your tools (functions) in one place,
and you open that toolbox whenever you need them.

---

## What is Import?

`import` is how you bring code from one file into another.

Example:
```python
from my_math import add
```

This line says: "Go to my_math.py and bring the add function here."

After this, you can use `add()` in your current file like normal.

---

## What is a Custom Module?

A custom module is a module YOU made yourself.

In this project, `my_math.py` is our custom module.
It has three functions: `add`, `subtract`, and `multiply`.

We made it ourselves, so it's "custom".
Python did not come with it — we wrote it.

Steps to create a custom module:
1. Create a new `.py` file (example: `my_math.py`)
2. Write your functions inside it
3. In another file, use `import` to bring those functions in

---

## What is a Third-Party Package?

A third-party package is code made by someone else that you download and use.

Python comes with some built-in stuff (like `math` or `random`).
But third-party packages are extra — you have to install them using `pip`.

In this project, we used `colorama`.
- We did NOT write colorama
- Someone else built it
- We installed it with: `pip install colorama`
- Then we imported it and used it

Other popular third-party packages you might hear about:
- `requests` — for working with websites
- `pandas` — for working with data
- `flask` — for building web apps
