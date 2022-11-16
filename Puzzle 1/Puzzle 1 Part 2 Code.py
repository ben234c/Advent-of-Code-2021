# Advent of Code 2021 Puzzle 1 Part 2

import fileinput
puzzleinput = fileinput.input(files='./puzzle1input.txt')
inputlist = []
increase = 0


for line in puzzleinput:
    inputlist.append(int(line)) # Separate inputs into individual elements and append them to an empty list (inputlist)

for i in range(len(inputlist)): # Using range(len(list)) method avoids various issues with duplicate numbers in different places
    firstelement = inputlist[i]
    oneback = inputlist[i - 1]
    twoback = inputlist[i - 2]
    threeback = inputlist[i - 3]
    firstwindow = threeback + twoback + oneback 
    secondwindow = twoback + oneback + firstelement
    if secondwindow > firstwindow:
        increase += 1

print(increase)