#!/usr/local/bin/python3
depthList = []
count = 0
last = 999999999
for line in open("input.txt"):
    depthList.append(line.rstrip())
    if int(line.rstrip()) > int(last): count += 1
    last=line.rstrip()
print(count)
