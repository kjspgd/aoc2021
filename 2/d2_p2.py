#!/usr/local/bin/python3
input = []
x_pos = 0
depth = 0
last = 0
for line in open("input.txt"):
    input.append(str(line.rstrip()))
for item in input:
    #print(item.split()[0]+ "," + item.split()[1])
    if item.split()[0] == "forward" : x_pos += int(item.split()[1])
    if item.split()[0] == "up" : depth -= int(item.split()[1])
    if item.split()[0] == "down" : depth += int(item.split()[1])

print(x_pos * depth)
