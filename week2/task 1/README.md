# File Handler

A simple Python project that reads a file and saves user quotes.
Made as part of my internship task.

---

## What It Does

- Reads a text file and counts the total number of words
- Asks the user for 3 favorite quotes and saves them to a file
- New quotes are added every time the program is run (nothing gets deleted)

---

## Files

```
task 1/
├── src/
│   ├── read_file.py      # reads input.txt and counts words
│   └── write_file.py     # saves user quotes to quotes.txt
├── data/
│   ├── input.txt         # sample text file to read
│   └── quotes.txt        # created automatically when write_file.py runs
├── docs/
│   └── file_modes.md     # explains r, w, a file modes
├── README.md
└── .gitignore
```

---

## How to Run

1. Make sure Python is installed.
2. Open a terminal and go to the `src` folder:

```
cd src
```

3. To count words from input.txt:

```
python read_file.py
```

4. To save your favorite quotes:

```
python write_file.py
```

---

## What to Expect

**read_file.py output:**
```
File read successfully!
Total word count: 45
```

**write_file.py output:**
```
Enter your 3 favorite quotes:
Quote 1: ...
Quote 2: ...
Quote 3: ...

3 quotes have been saved to '../data/quotes.txt'.
Done! You can run this program again to add more quotes.
```

---

## Notes

- `quotes.txt` is created automatically in the `data` folder on first run.
- Running `write_file.py` multiple times keeps adding quotes — it never overwrites.
- If `input.txt` is missing, the program will show a clear error message.

---

## Requirements

- Python 3.x
- No external libraries needed
