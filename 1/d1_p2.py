#!/usr/local/bin/python3
input = []
count = 0
linecount = 0
last = 0
for line in open("input.txt"):
    input.append(int(line.rstrip()))
for item in input:
    if len(input[linecount:linecount+3]) == 3 and sum(input[linecount:linecount+3]) > last and linecount != 0 : count+=1
    last = sum(input[linecount:linecount+3])
    linecount += 1
print(count)
