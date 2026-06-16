# Control Flow in Python Report

**Intern Name:** _(Your Name)_

---

## 1. Objective

In this task I learned how to use conditional statements and loops in Python. I made two programs — one that checks numbers and one that does loop operations.

---

## 2. What I Did

### number_checks.py

This program asks the user to enter a number and then:
- Checks if the number is even or odd
- Checks if the number is positive, negative, or zero

I used `if`, `elif`, and `else` for this. I also used `try/except` so the program doesn't crash if someone types a word instead of a number.

### loop_operations.py

This program has three things:
- Prints a multiplication table for any number the user enters
- Calculates the sum of first N natural numbers
- Prints a star pattern

I used `for` loop and `range()` for all three of these.

---

## 3. How the Code Works

**Even or Odd check:**
```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```
The `%` operator gives the remainder. If the remainder is 0 the number is even.

**Positive, Negative, Zero check:**
```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Multiplication table:**
```python
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Sum of N numbers:**
```python
total = 0
for i in range(1, n + 1):
    total += i
```

**Star pattern:**
```python
for i in range(1, n + 1):
    print("* " * i)
```

---

## 4. Test Cases

| Input | Output |
|---|---|
| `4` | Even, Positive |
| `7` | Odd, Positive |
| `-5` | Odd, Negative |
| `0` | Even, Zero |
| `abc` | Shows error message |

Screenshots of all outputs are saved in `docs/screenshots/`.

---

## 5. What I Learned

- How to use `if`, `elif`, `else` in Python
- How `for` loop works with `range()`
- How to take input from the user
- How to handle wrong input using `try/except`
- How to print patterns using loops

---

## 6. Conclusion

This was a good task for understanding the basics of Python. Conditional statements and loops are used in almost every program so it was helpful to practice them with simple examples.
