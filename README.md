# APcompsciportfolio
This is the portfolio of some of my AP CSP files.
# README 1 — Password.py

"""
Project: Password Authentication Loop
-------------------------------------

This program repeatedly asks the user for a password until the correct one is entered.

How It Works:
- Runs an infinite loop using `while True`.
- Prompts the user to enter a password.
- If the user types "boi", access is granted and the loop ends.
- Any other input prints "incorrect password" and repeats.

Features:
- Simple authentication loop
- Uses conditional logic and looping
- Demonstrates input handling

How to Run:
    python password.py

Example:
    Enter the password: hi
    incorrect password
    Enter the password: boi
    access granted
"""
# README 2 — Gamedevstories.py

"""
Project: Data Filtering with Pandas
-----------------------------------

This program loads a CSV file (dev.csv) and performs several filtering operations
on influencer story data.

How It Works:
- Reads the CSV using pandas.read_csv().
- Extracts columns into lists: Level, Time, Rating, Summary, Feedback.
- Defines three filtering functions:
    abnormal(ti, rate) — finds entries with time > ti and rating > rate.
    secret(word) — finds entries where feedback contains a keyword.
    problems(rate) — finds entries with rating below a threshold.
- Prints matching row indices and displays specific rows using data.loc.

Features:
- CSV loading
- List-based filtering
- Keyword search
- Conditional logic

How to Run:
    python influencer_stories.py

Example Operations:
    abnormal(100, 4.5)
    secret("secret")
    problems(2)
"""
# README 3 — Adventure.py

"""
Project: Interactive Movie/TV Show Recommender
----------------------------------------------

This program simulates a simple theater assistant that recommends movies or TV shows
based on user choices.

How It Works:
- Asks whether the user wants a movie or tv show.
- If movie:
      asks for horror or comedy and recommends a title.
- If tv show:
      asks for rom-com or action and recommends a title.
- Uses nested conditionals to determine the output.

Features:
- Interactive text-based menu
- Genre-based recommendations
- Simple branching logic

How to Run:
    python theater.py

Example:
    Would you like to watch a movie or tv-show? movie
    Got it, would you like to watch a horror or comedy movie? comedy
    I suggest you go see white chicks.
"""
# README 4 — Race(1).py

"""
Project: Tortoise vs. Hare Simulation
-------------------------------------

This program simulates 10,000 races between a tortoise and a hare to compare win rates.

How It Works:
- Hare:
    - 43% chance of falling asleep each turn.
    - If awake, moves 1–10 meters.
- Tortoise:
    - Always moves 1–3 meters.
- First to reach 50 meters wins.
- simulation(trials) runs many races and counts wins.

Key Functions:
- race() — runs a single race.
- sleepy_hare() — determines if hare sleeps.
- hare_movement() — moves hare.
- tortoise_movement() — moves tortoise.
- simulation(10000) — runs 10,000 trials.

Features:
- Randomized movement
- Probability-based behavior
- Large-scale simulation

How to Run:
    python race.py

Example Output:
    Tortoise Wins | 6234
    Hare Wins | 3766
"""
# README 5 — Grocery Store Price Checker

"""
Project: Grocery Price Tools
----------------------------

This program stores a list of grocery items and prices, applies discounts,
checks prices, and lists items within a budget.

How It Works:
- Two lists store items and prices.
- discount(decimal) applies a percentage discount to all prices.
- price_check(item_name) returns the price of a specific item.
- budget(cost) prints all items cheaper than or equal to the given cost.
- Main script:
      - Applies a 20% discount.
      - Lists items under $2.00.
      - Calculates total cost of several items.

Features:
- Bulk price modification
- Item lookup
- Budget filtering
- Total cost calculation

How to Run:
    python grocery.py

Example Output:
    Milk
    Eggs
    ...
    12.3456
"""
