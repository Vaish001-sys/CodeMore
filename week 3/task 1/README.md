# Week 3 – Task 1: Python Dictionaries

This task is about learning how dictionaries work in Python.  
There are two programs — one that shows the basics, and one mini project (a contact book).

---

## What's Inside

```
task 1/
│
├── src/
│   ├── dictionary_basics.py   # Shows basic dictionary operations
│   └── contact_book.py        # Mini project: a simple contact book
│
├── docs/
│   └── dictionary_notes.md    # Notes on how dictionaries work
│
└── README.md
```

---

## How to Run

Make sure you have Python installed. Open a terminal in the `task 1` folder and run:

**Program 1 – Dictionary Basics:**
```
python src/dictionary_basics.py
```

**Program 2 – Contact Book:**
```
python src/contact_book.py
```

No extra libraries needed. Just plain Python.

---

## Sample Output

### dictionary_basics.py

```
========================================
       DICTIONARY BASICS DEMO
========================================

[1] Creating dictionary...
    Dictionary created: {'name': 'Alice', 'age': 20, 'grade': 'A', 'subject': 'Python'}

[2] Adding items...
Added 'email' and 'city' to the dictionary.

[3] Updating items...
Updated 'age' and 'grade' in the dictionary.

[4] Iterating through dictionary...

--- All Key-Value Pairs ---
  name: Alice
  age: 21
  grade: A+
  subject: Python
  email: alice@example.com
  city: Mumbai

[5] Printing keys and values separately...

--- Keys ---
  name
  age
  grade
  subject
  email
  city

--- Values ---
  Alice
  21
  A+
  Python
  alice@example.com
  Mumbai

[6] Now it's your turn — enter your own student data!

--- Enter Your Student Info ---
Enter student name: Rahul
Enter student marks (out of 100): 88

--- Stored Result ---
  name: Rahul
  marks: 88

========================================
          DEMO COMPLETE
========================================
```

---

### contact_book.py

```
Welcome to the Contact Book!

===================================
        CONTACT BOOK MENU
===================================
  1. Add Contact
  2. Search Contact
  3. Display All Contacts
  4. Delete Contact
  5. Exit
===================================
Enter your choice (1-5): 1

--- Add Contact ---
Enter name: Priya
Enter phone number: 9876543210
Enter email address: priya@gmail.com
Contact 'Priya' added successfully!

===================================
Enter your choice (1-5): 2

--- Search Contact ---
Enter name to search: Priya

Contact Found:
  Name  : Priya
  Phone : 9876543210
  Email : priya@gmail.com

===================================
Enter your choice (1-5): 3

--- All Contacts ---
No.   Name                 Phone           Email
------------------------------------------------------------
1     Priya                9876543210      priya@gmail.com

===================================
Enter your choice (1-5): 4

--- Delete Contact ---
Enter name to delete: Priya
Contact 'Priya' deleted successfully!

===================================
Enter your choice (1-5): 5

Goodbye! Your contacts will not be saved after exit.
```

---

## Notes

- Contacts are stored only while the program is running. They are lost when you exit.
- The dictionary basics program runs automatically and shows each step.
- See `docs/dictionary_notes.md` for a simple explanation of how dictionaries work.
