The files in this repository are set up exclusively for the ISM3232 Midterm project in the fall of 2026.

The exam requires me to follow the instructions based on the first letter of my last name. Since my name has two words, I opted to go with D in 'De Mesquita'.

# ISM3232 Midterm: Harvest Table Catering

- **Name:** Mateus De Mesquita
- **Version:** 1.0
- **Date:** (the day you finish)

## What This Program Does
This program prices catering events for Harvest Table Catering. It applies the company's discount, service fee, sign-off, and second-chef rules to a list of events. It then prints a report with one line per event and a summary of the totals.

## Business Rules
- Food cost is the price per guest times the number of guests.
- Events with 25 to 99 guests get 5% off, and events with 100 or more get 12% off, but only if the client is a registered nonprofit. Other 100+ guest events get 5%.
- Events with fewer than 25 guests get no discount.
- A $75 service fee is added when the discounted cost is $500 or less.
- An event total over $2,500 needs a manager's sign-off.
- An event needs a second chef when it has more than 80 guests or its total is $3,000 or more.

## How to Run
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```
ruff format .
ruff check .
pytest -v
```
I wrote 25 tests.

## Files in This Repository
- `business_rules.py`: the eight business-rule functions
- `main.py`: builds the report from the list of events
- `commands.md`: a record of the terminal commands and their output
- `README.md`: this file
- `requirements.txt`: the packages needed (pytest and ruff)
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository
- `tests/__init__.py`: marks the tests folder as a package
- `tests/test_business_rules.py`: my pytest tests for the functions

## AI Use Statement
I did not use AI on this exam.