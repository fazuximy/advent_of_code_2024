import pandas as pd
import numpy as np
from pathlib import Path


# Day 1
print("Day 1 Solutions\n")

# Importing Data

input_file_name = "input.txt" 
input_data_path = Path(__file__).parent / "data"
input_file_path = input_data_path / input_file_name

with open(input_file_path) as f:
    data = f.read().splitlines()

# Cleaning Data

location_id_group_1 = []
location_id_group_2 = []

for data_line in data:
    split_numbers = data_line.split("  ")

    location_id_group_1.append(int(split_numbers[0]))
    location_id_group_2.append(int(split_numbers[1]))


# Task 1
print("Task 1:")

"""
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

    The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
    The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
    The third-smallest number in both lists is 3, so the distance between them is 0.
    The next numbers to pair up are 3 and 4, a distance of 1.
    The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
    Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.

To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
"""


sorted_location_id_group_1 = np.sort(location_id_group_1)

sorted_location_id_group_2 = np.sort(location_id_group_2)

distance_between_locations = np.abs(np.subtract(sorted_location_id_group_1,sorted_location_id_group_2))

summed_distance_between_locations = np.sum(distance_between_locations)

print(f"The total distance betwen the lists is: {summed_distance_between_locations}\n")


# Task 2
print("Task 2:")

"""
The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Once again consider your left and right lists. What is their similarity score?
"""

similary_scores = []

for location_id in sorted_location_id_group_1:

    location_id_count = np.count_nonzero(sorted_location_id_group_2 == location_id)

    similarity_score = location_id_count * location_id

    similary_scores.append(similarity_score)

summed_similarity_scores = np.sum(similary_scores)
print(f"The similarity score is: {summed_similarity_scores}\n")