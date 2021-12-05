#!/usr/local/bin/python3
from collections import Counter
startPos = []
endPos = []
usedPoints = []



def completeLine(incStart, incEnd):
    returnList = []
    x1 = incStart[0]
    x2 = incEnd[0]
    y1 = incStart[1]
    y2 = incEnd[1]
    if x1>x2:
        x1 = incEnd[0]
        x2 = incStart[0]
    if y1>y2:
        y2 = incStart[1]
        y1 = incEnd[1]
    if x1==x2:
        for i in range (y1,y2+1): returnList.append([x1,i])
    elif y1==y2:
        for i in range (x1,x2+1): returnList.append([i,y1])
    #print(returnList)
    #input("Debug to continue")
    return returnList


for line in open("input.txt"):
    startPos = list(map(int, line.rstrip().split(" -> ")[0].split(",")))
    endPos = list(map(int, line.rstrip().split(" -> ")[1].split(",")))
    #print(str(startPos) + " >> " + str(endPos))
    #print(completeLine(startPos, endPos))
    usedPoints += completeLine(startPos, endPos)

#this is dumb because evidently you can't set a list of lists (unhashable)
strPoints = []
for coord in usedPoints:
    strPoints.append(str(coord[0])+":"+str(coord[1]))
#print(strPoints)

'''
count = 0
dupes = set()
uniqs = []
progress = 0
for coord in set(strPoints):
    print(progress/len(strPoints)*100)
    progress +=1
    if strPoints.count(coord)>1: count+=1
'''

count =0
progress = 0
countDict = Counter(strPoints)
for dictItem in countDict.keys():
    print(progress/len(strPoints)*100)
    progress +=1
    if countDict[dictItem]>1: count +=1


print("----")
print(len(usedPoints))
print(len(strPoints))
print(len(list(set(strPoints))))
print(len(strPoints)-len(list(set(strPoints))))
print("---")
#print(len(list(set(uniqs))))
#print(len(list(dupes)))
print(count)