# Dictionary Notes

These are my notes on Python dictionaries from Week 3 of my internship.

---

## What is a Dictionary?

A dictionary is a way to store information in Python using **pairs**.  
Each pair has a **key** and a **value**.

Think of it like a real dictionary:
- The **word** is the key
- The **meaning** is the value

Example:

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

Here, `"name"`, `"age"`, and `"grade"` are the **keys**.  
`"Alice"`, `20`, and `"A"` are the **values**.

---

## Key-Value Pairs

Every item in a dictionary is a key-value pair.

- The key is always on the **left**
- The value is always on the **right**
- They are separated by a **colon** `:`
- Each pair is separated by a **comma** `,`

```python
person = {
    "name": "Rahul",   # key: "name", value: "Rahul"
    "city": "Mumbai"   # key: "city", value: "Mumbai"
}
```

You can access any value using its key:

```python
print(person["name"])   # Output: Rahul
print(person["city"])   # Output: Mumbai
```

---

## Adding Data

You can add a new key-value pair to an existing dictionary like this:

```python
student = {"name": "Alice"}

student["marks"] = 95       # Adding a new key called "marks"
student["subject"] = "Math" # Adding another new key

print(student)
# Output: {'name': 'Alice', 'marks': 95, 'subject': 'Math'}
```

Just write the dictionary name, then the new key in square brackets, and assign a value.

---

## Updating Data

Updating works the same way as adding — you just use a key that already exists.

```python
student = {"name": "Alice", "grade": "B"}

student["grade"] = "A"   # This updates the existing "grade" value

print(student)
# Output: {'name': 'Alice', 'grade': 'A'}
```

If the key already exists, Python replaces the old value with the new one.  
If the key does not exist, Python adds it as a new item.

---

## Iterating Through a Dictionary

Iterating means going through the dictionary one item at a time.

### Print all keys and values together:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Alice
# age : 20
# grade : A
```

### Print only keys:

```python
for key in student.keys():
    print(key)

# Output:
# name
# age
# grade
```

### Print only values:

```python
for value in student.values():
    print(value)

# Output:
# Alice
# 20
# A
```

---

## Quick Summary

| What you want to do | How to do it |
|---|---|
| Create a dictionary | `d = {"key": "value"}` |
| Access a value | `d["key"]` |
| Add a new item | `d["new_key"] = "new_value"` |
| Update an item | `d["existing_key"] = "new_value"` |
| Loop through all items | `for k, v in d.items()` |
| Loop through keys only | `for k in d.keys()` |
| Loop through values only | `for v in d.values()` |
