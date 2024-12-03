import re
from pathlib import Path


# Day 3
print("Day 3 Solutions\n")

# Importing Data

input_file_name = "input.txt" 
input_data_path = Path(__file__).parent / "data"
input_file_path = input_data_path / input_file_name

with open(input_file_path) as f:
    data = f.read()


# Task 1
print("Task 1:")

"""
It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

found_muls = re.findall("mul\(\d+\,\d+\)",data)

muls = []
for found_mul in found_muls:

    numbers = re.findall("\d+",found_mul)

    muls.append(int(numbers[0])*int(numbers[1]))

print(f"The sum of the multiplication results are: {sum(muls)}\n")


# Task 2
print("Task 2:")

"""
There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""


found_do_and_donts = re.finditer("mul\(\d+\,\d+\)|(do\(\))|(don\'t\(\))",data)

enable_mul = True

enabled_muls = []

for found in found_do_and_donts:

    if "don't()" == found[0]:
        enable_mul = False

    elif "do()" == found[0]:
        enable_mul = True

    else:

        if enable_mul:

            numbers = re.findall("\d+",found[0])
            enabled_muls.append(int(numbers[0])*int(numbers[1]))


print(f"The sum of the enabled multiplications is: {sum(enabled_muls)}")