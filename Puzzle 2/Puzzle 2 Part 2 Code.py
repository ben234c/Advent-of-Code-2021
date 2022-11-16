# Advent of Code 2021 Puzzle 2 Part 2

import fileinput
puzzleinput = fileinput.input(files='./puzzle2input.txt')
inputlist = []
horipos = 0
depth = 0
aim = 0

for line in puzzleinput:
    inputlist.append(line) # Separate inputs into individual elements and append them to an empty list (inputlist)

for i in range(len(inputlist)):
    command = inputlist[i].split() # Separates direction and number
    print(command)

    if command[0] == 'up': # Check direction
        aim -= int(command[1])

    if command[0] == 'down':
        aim += int(command[1])
    
    if command[0] == 'forward':
        horipos += int(command[1])
        depth += aim * int(command[1])

finalpos = horipos * depth

print('results')
print(horipos)
print(depth)
print(finalpos)

