# Python Syntax Notes

These are my personal notes from Week 2. Written in simple language so I can come back and understand them later.

---

## Variables

A variable is just a box that stores a value.

You give it a name, and then put something inside it using `=`.

```python
name = "Alice"
age = 20
```

Now whenever you type `name`, Python knows you mean `"Alice"`.

**Rules for naming variables:**
- No spaces (use `_` instead, like `my_name`)
- Can't start with a number
- Case sensitive — `Age` and `age` are different things

---

## Data Types

Every value in Python has a type. The type tells Python what kind of data it is.

### str (String)
Text. Always goes inside quotes.

```python
language = "Python"
```

### int (Integer)
A whole number. No quotes, no decimal point.

```python
age = 20
```

### float (Float)
A number with a decimal point.

```python
gpa = 8.75
```

### bool (Boolean)
Either `True` or `False`. Nothing else. Capital T and F.

```python
is_student = True
```

---

### How to check the type of a variable

Use `type()` and wrap your variable inside it.

```python
print(type(age))       # <class 'int'>
print(type(language))  # <class 'str'>
```

---

## Indentation

Indentation means the spaces at the start of a line.

In Python, indentation is **not optional**. It tells Python which lines belong together.

**Example — without indentation (wrong):**
```python
if True:
print("hello")   # this will crash
```

**Example — with indentation (correct):**
```python
if True:
    print("hello")   # 4 spaces before print
```

The standard is **4 spaces** per level.

Every time you open a block (after `if`, `for`, `def`, etc.) you add one level of indentation. When the block ends, you go back.

```python
if age > 18:
    print("adult")       # inside the if block
    print("can vote")    # still inside
print("this is outside") # back to normal
```

---

> Tip: Most code editors (like VS Code) add the 4 spaces automatically when you press Enter after a colon.
