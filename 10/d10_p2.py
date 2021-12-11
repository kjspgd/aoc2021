#!/usr/local/bin/python3
lineList = []
count = 0
valids = ['()','[]','{}','<>']
part1_scoreDict = {}
part1_scoreDict[')']=3
part1_scoreDict[']']=57
part1_scoreDict['}']=1197
part1_scoreDict['>']=25137
for line in open("input.txt"):
    lineList.append(line.rstrip())
#print(lineList)


shortenedLineList = []
for line in lineList:
    run = True
    workingString = line
    print("Checking: " + workingString)
    for i in range(0,len(line)):
    #while run:
        startLen = len(workingString)
        for valid in valids:
            #print(valid)
            #print(workingString)
            workingString = workingString.replace(valid,'')
            if len(workingString)==startLen: run: False
    shortenedLineList.append(workingString)

score = 0
for short in shortenedLineList:
    for token in short:
        if token in part1_scoreDict.keys():
            print("Winner" + " " + token)
            score += part1_scoreDict[token]
            break
print(score)