#!/usr/local/bin/python3
import statistics
median = 0
inputList = []
fuelConsumption = 0

for line in open("sample_input.txt"):
    for val in line.rstrip().split(","):
        inputList.append(int(val))

median = statistics.median(inputList)

for val in inputList:
    fuelConsumption += abs(median - val)

print(median)
print(fuelConsumption)
