#!/usr/local/bin/python3
count = 0
debug = 0
for line in open("input.txt"):
    for item in line.rstrip().split("|")[1].split():
        if debug: print(item + ": + " + str(len(item)))
        if len(item) in [2,3,4,7]: count += 1
print(count)