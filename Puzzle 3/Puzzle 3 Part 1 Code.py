# Advent of Code 2021 Puzzle 3 Part 1

import fileinput
puzzleinput = fileinput.input(files='./puzzle3input.txt')
inputlist = []

for line in puzzleinput:
    inputlist.append(line) # Separate inputs into individual elements and append them to an empty list (inputlist)