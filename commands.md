# Terminal Record: 	Harvest Table Catering

## 1. Building the project

'''
cd
mkcd ism3232_midterm
git init
env
act
pipi pytest ruff
mkdir tests
touch business_rules.py main.py commands.md README.md .gitignore tests/__init__.py tests/test_business_rules.py
code .gitignore
pip freeze > requirements.txt
git remote add origin https://github.com/demesquitamateus/ism3232-midterm.git
'''





## 2. The virtual environment

```
which python3
```

```
/Users/demateus/ism3232_midterm/.venv/bin/python3
```

The .venv shows that the virtual environment is now active.

## 3. The project structure
.
├── __pycache__
│   └── business_rules.cpython-312.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

Pycache is not in the repo because it was included in the gitignore

## 4. Every function and test
business_rules.py
15:def calculate_food_cost(guest_price: float, guests: int) -> float:
19:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
29:def calculate_event_total(
40:def needs_signoff(total: float) -> bool:
44:def needs_second_chef(guests: int, total: float) -> bool:
48:def total_booked(events: list) -> float:
58:def largest_event(events: list) -> str:
72:def format_event_line(

tests/test_business_rules.py
13:def test_food_cost_multiplies_price_by_guests():
17:def test_no_discount_at_24_guests():
21:def test_five_percent_discount_at_25_guests():
25:def test_five_percent_discount_at_99_guests():
29:def test_regular_event_gets_five_percent_at_100_guests():
33:def test_nonprofit_gets_twelve_percent_at_100_guests():
37:def test_nonprofit_gets_only_five_percent_at_99_guests():
41:def test_service_fee_added_at_exactly_500():
45:def test_no_service_fee_just_above_500():
49:def test_event_total_applies_discount_then_fee():
53:def test_nonprofit_flag_changes_event_total():
60:def test_no_signoff_at_exactly_2500():
64:def test_signoff_needed_just_above_2500():
68:def test_no_second_chef_at_80_guests():
72:def test_second_chef_needed_at_81_guests():
76:def test_no_second_chef_just_below_3000_total():
80:def test_second_chef_needed_at_exactly_3000_total():
84:def test_total_booked_adds_every_event_total():
92:def test_total_booked_of_empty_list_is_zero():
96:def test_largest_event_returns_client_with_biggest_total():
105:def test_largest_event_tie_returns_first_in_list():
113:def test_largest_event_of_empty_list_is_empty_string():
117:def test_format_event_line_shows_no_for_false_values():
122:def test_format_event_line_shows_yes_for_true_values():
127:def test_format_event_line_always_has_two_decimals():

It defines 25 tests and 8 functions.


## 5. Which files print
main.py

It doesnt show business rules because there are no print functions in business rules

## 6. The commit history
6d2be9a (HEAD -> main, origin/main) changed the readme and commands file for grading
95ffe64 main.py prints and imports with testing and commands
750d20e format event line added and tested
a9d2c8f Add total_booked and largest_event using for loops, with tests
ae270f8 pasted code and texts from desktop computer into the files from previous working session up to needs second chef and needs signoff
fce8f7e event rules tests and business rules updated to calculate_event_total
4c1495a business rules with functions and constants inserted
d68d514 commands pasted into main and the commands file reenacted with the setup commands
584ab9d Installed directory and packages. Set up the venv and correct files and repositories
2be1293 ISM3232 Git Repo Setup - Testing the repo to see if it works with general readme information

There are 10 commits at this point.

