#!/usr/local/bin/python3
from collections import Counter
importDict = {}
val=""
inverse=""
for x in range(0,12):
    importDict[x] = []

for line in open("input.txt"):
    for x in range(0,12):
        importDict[x].insert(len(importDict[x]),int(line.rstrip()[x]))

for key in importDict.keys():
    if sum(importDict[key]) > len(importDict[key])/2:
        val += "1"
        inverse += "0"

    else:
        val += "0"
        inverse += "1"
print(int(val,2)*int(inverse,2))
