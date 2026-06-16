"""
user_input.py
-------------
This script takes input from the user (name, age, favourite language),
prints a personalized greeting, and calculates the year they will turn 100.
"""

import datetime  # We need this to get the current year

if __name__ == "__main__":

    # ── Get current year automatically ───────────────────────────────────────
    current_year = datetime.datetime.now().year

    # ── Ask the user for information ─────────────────────────────────────────
    print("===== Tell me about yourself =====")

    name     = input("What is your name? ")                        # string input
    age      = int(input("How old are you? "))                     # convert to int
    language = input("What is your favourite programming language? ")  # string input

    print()  # blank line

    # ── Print a personalized greeting ─────────────────────────────────────────
    print("===== Hello! =====")
    print(f"Hi {name}! Great to meet you.")
    print(f"You are {age} years old and you love {language}. Awesome choice!")

    print()  # blank line

    # ── Calculate the year the user will turn 100 ─────────────────────────────
    years_left      = 100 - age               # how many years until they are 100
    year_turn_100   = current_year + years_left  # add to the current year

    print("===== Fun Fact =====")

    if years_left > 0:
        print(f"You will turn 100 years old in the year {year_turn_100}!")
    elif years_left == 0:
        print("Wow, you are turning 100 this year! Happy 100th birthday!")
    else:
        # age is already over 100
        print(f"You already passed 100! You turned 100 back in {year_turn_100}.")
