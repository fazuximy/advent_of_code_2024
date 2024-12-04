import numpy as np
from pathlib import Path

# Day 4
print("Day 4 Solutions\n")

# Importing Data

input_file_name = "input.txt" 
input_data_path = Path(__file__).parent / "data"
input_file_path = input_data_path / input_file_name

with open(input_file_path) as f:
    data_lines = f.read().splitlines()

character_lists = []
for line in data_lines:
    character_lists.append(list(line))

character_matrix = np.array(character_lists)

# Task 1
print("Task 1:")

"""
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

Take a look at the little Elf's word search. How many times does XMAS appear?
"""


coord_offsets = np.array([[1,0],[0,1],[0,-1],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]])

xmas_counter = 0

for y_num in range(0,character_matrix.shape[0]):
    for x_num in range(0,character_matrix.shape[1]):

        current_character = character_matrix[x_num,y_num]

        if current_character == "X":

            current_coord = np.array([x_num,y_num])

            surrounding_coordinates = [coord_offset+current_coord for coord_offset in coord_offsets]

            new_coord_offsets, surrounding_coordinates = zip(*[(coord_offset, coord) for coord_offset, coord in zip(coord_offsets,surrounding_coordinates) if all(coord < character_matrix.shape[0]) and all(coord >= 0)])

            for new_coord_offset,coord in zip(new_coord_offsets,surrounding_coordinates):

                if character_matrix[coord[0],coord[1]] == "M":
                    new_coord = coord + new_coord_offset

                    if (any(new_coord >= character_matrix.shape[0]) or any(new_coord < 0)):
                        continue

                    if (character_matrix[new_coord[0],new_coord[1]] == "A"):
                        new_coord = new_coord + new_coord_offset

                        if (any(new_coord >= character_matrix.shape[0]) or any(new_coord < 0)):
                            continue

                        if (character_matrix[new_coord[0],new_coord[1]] == "S"):

                            xmas_counter += 1

print(f"XMAS appear {xmas_counter} times\n")



# Task 2
print("Task 2:")

"""
Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""


mas1_offset = np.array([[1,1],[-1,-1]])
mas2_offset = np.array([[1,-1],[-1,1]])

x_mas_counter = 0

for y_num in range(0,character_matrix.shape[0]):
    for x_num in range(0,character_matrix.shape[1]):

        current_character = character_matrix[x_num,y_num]

        if current_character == "A":

            current_coord = np.array([x_num,y_num])

            mas1_coordinates = [coord_offset+current_coord for coord_offset in mas1_offset]
            
            mas2_coordinates = [coord_offset+current_coord for coord_offset in mas2_offset]

            mas1_coordinates = [coord for coord in mas1_coordinates if all(coord < character_matrix.shape[0]) and all(coord >= 0)]

            mas2_coordinates = [coord for coord in mas2_coordinates if all(coord < character_matrix.shape[0]) and all(coord >= 0)]

            mas1_correct = False
            mas2_correct = False

            if len(mas1_coordinates) == 2: 

                mas1_letters = set([character_matrix[mas1_coordinates[0][0],mas1_coordinates[0][1]][0], character_matrix[mas1_coordinates[1][0],mas1_coordinates[1][1]][0]])
                mas1_correct = mas1_letters == set(["M","S"])

            if len(mas2_coordinates) == 2: 
                mas2_letters = set([character_matrix[mas2_coordinates[0][0],mas2_coordinates[0][1]][0], character_matrix[mas2_coordinates[1][0],mas2_coordinates[1][1]][0]])
                mas2_correct = mas2_letters == set(["M","S"])

            if mas1_correct and mas2_correct:
                x_mas_counter += 1

print(f"X-MAS (cross MAS) appears {x_mas_counter} times")


