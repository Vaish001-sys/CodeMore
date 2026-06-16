# OOP Notes (Object Oriented Programming)

These are my personal notes from Week 3 of my internship.
I tried to write them in a way that actually makes sense to me.

---

## 1. What is a Class?

A class is like a **blueprint** or a **template**.

Think of it like a cookie cutter. The cookie cutter is the class.
It doesn't eat anything — it just defines the *shape*.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here, `Student` is the class. It says "every student will have a name and an age."

---

## 2. What is an Object?

An object is what you actually create using the class (the blueprint).

Using the cookie cutter, you make actual cookies. Those cookies are objects.

```python
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
```

`student1` and `student2` are objects (also called instances) of the `Student` class.
Each one has its own name and age.

> Simple way to remember:
> **Class = recipe, Object = the dish you cook from that recipe**

---

## 3. What is Inheritance?

Inheritance is when one class **gets the features of another class**.

Like how a child inherits things from their parents (eye color, height, etc.),
a child class inherits methods and attributes from a parent class.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # child classes will fill this in

# Child class
class Dog(Animal):    # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} says: Woof!")
```

`Dog` doesn't need to rewrite `__init__` — it already got it from `Animal`.
This saves repetition and keeps things organized.

> Simple way to remember:
> **Inheritance = copy-paste, but smarter**

---

## 4. What is Polymorphism?

Polymorphism sounds fancy but the idea is simple.

It means **same method name, different behavior** depending on which class is using it.

```python
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")
```

Both `Dog` and `Cat` have a method called `speak()`.
But when you call it, each one responds differently.

```python
animals = [Dog("Rex"), Cat("Luna"), Dog("Max")]

for animal in animals:
    animal.speak()   # Python figures out which speak() to use automatically
```

Output:
```
Rex says: Woof!
Luna says: Meow!
Max says: Woof!
```

> Simple way to remember:
> **Polymorphism = one remote, works on different TVs differently**

---

## Quick Summary Table

| Concept | What it means | Real-life example |
|---|---|---|
| Class | A blueprint/template | Cookie cutter |
| Object | A thing made from the class | An actual cookie |
| Inheritance | Child class gets parent features | Kid inherits parent traits |
| Polymorphism | Same method, different behavior | Same word, different meaning in context |

---

*Written during Week 3 internship task — kept simple on purpose!*
