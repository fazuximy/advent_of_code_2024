import pandas as pd
import numpy as np
from pathlib import Path


# Day 1
print("Day 2 Solutions\n")

# Importing Data

input_file_name = "input.txt" 
input_data_path = Path(__file__).parent / "data"
input_file_path = input_data_path / input_file_name

with open(input_file_path) as f:
    data = f.read().splitlines()

# Cleaning Data


# Task 1
print("Task 1:")

"""
The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""

level_groups = []
level_difference_groups = []

acceptable_level_differences = 0

for data_line in data:
    split_numbers = data_line.split(" ")

    levels = [int(numb) for numb in split_numbers]

    level_differences = [level-levels[numb] for numb,level in enumerate(levels[1:])]

    # Checks all the diffrences either 1, 2, 3 or -1, -2, -3
    if set(level_differences) <= {1, 2, 3} or set(level_differences) <= {-1, -2, -3}:
        acceptable_level_differences += 1

    level_difference_groups.append(level_differences)
    level_groups.append(levels)

level_differences_df = pd.DataFrame(level_difference_groups)

print(f"{np.sum(acceptable_level_differences)} reports are safe\n")


# Task 2
print("Task 2:")

"""
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

def is_level_safe(levels):

    level_diff = []
    for level_numb in range(len(levels) - 1):

        level_diff.append(levels[level_numb + 1] - levels[level_numb])

    if set(level_diff) <= {1, 2, 3} or set(level_diff) <= {-1, -2, -3}:
        return True
    
    return False


safe_count = 0

for levels in level_groups:

    safe_level = []

    # Going through all possible removals
    for level_numb in range(len(levels)):

        safe_level.append(is_level_safe(levels[:level_numb] + levels[level_numb + 1:]))

    # If just one is possible, it's safe
    if any(safe_level):
        safe_count += 1


print(f"{safe_count} reports are safe with the dampener\n")


