# Advent of Code 2021 Puzzle 1 Part 1

import fileinput
puzzleinput = fileinput.input(files='./puzzle1input.txt')
inputlist = []
increase = 0


for line in puzzleinput:
    inputlist.append(int(line)) # Separate inputs into individual elements and append them to an empty list (inputlist)

for i in range(len(inputlist)): # Using range(len(list)) method avoids various issues with duplicate numbers in different places
    previndex = i - 1
    if inputlist[i] > inputlist[previndex]:
        increase += 1

print(increase)