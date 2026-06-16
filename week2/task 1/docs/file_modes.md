# File Modes in Python

When you open a file in Python, you have to tell it what you want to do with it.
This is called the **file mode**.

You set the mode inside the `open()` function like this:

```python
open("filename.txt", "mode")
```

There are three basic modes used in this project.

---

## r — Read Mode

- Used when you just want to **read** what is already in a file.
- It does **not** change or delete anything.
- If the file does not exist, Python will give an error.

**Example:**
```python
with open("input.txt", "r") as file:
    content = file.read()
```

Think of it like **opening a book to read** — you are not writing anything, just looking.

---

## w — Write Mode

- Used when you want to **create a new file** or **completely replace** what is in an existing file.
- If the file already exists, everything in it gets **deleted first**, then the new content is written.
- If the file does not exist, Python creates it for you.

**Example:**
```python
with open("output.txt", "w") as file:
    file.write("Hello!")
```

Think of it like **tearing out all pages of a notebook and starting fresh**.

---

## a — Append Mode

- Used when you want to **add new content to the end** of a file.
- It does **not** delete what is already there.
- If the file does not exist, Python creates it for you.

**Example:**
```python
with open("quotes.txt", "a") as file:
    file.write("A new quote.\n")
```

Think of it like **writing on the next blank page of a notebook** — everything before stays as it is.

---

## Quick Comparison

| Mode | Creates File? | Deletes Existing Content? | Use When |
|------|--------------|--------------------------|----------|
| r    | No           | No                       | Reading a file |
| w    | Yes          | Yes                      | Writing fresh content |
| a    | Yes          | No                       | Adding to existing content |

---

## Which Mode Is Used in This Project?

- `read_file.py` uses **r** to read `input.txt`
- `write_file.py` uses **a** to save quotes without overwriting old ones
