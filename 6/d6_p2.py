#!/usr/local/bin/python3

fishDict = {}
fishCount = len(fishDict.keys())
dayCount = 80

def createFish(incFishDict):
    print("Make a new Fish")
    return True

def fishProcessor(incDayCount):
    createFish=False
    returnDayCount = 0
    if incDayCount==0:
        returnDayCount = 6
        createFish = True
    else:
        returnDayCount = incDayCount - 1
    return returnDayCount, createFish

for line in open("input.txt"):
    for fishDays in map(int,line.rstrip().split(",")):
        fishDict[fishCount] = fishDays
        fishCount = len(fishDict.keys())

#print(fishDict)

addFish = 0
for day in range(0+1, dayCount+1):
    for i in range(0,addFish):
        fishDict[len(fishDict.keys()) + 1] = 9
    addFish = 0
    for fish in fishDict.keys():

        #print("----")
        #print(fishDict[fish])
        #print(fishProcessor(fishDict[fish])[0])
        #print("----")
        fishDict[fish] = fishProcessor(fishDict[fish])[0]
        if fishProcessor(fishDict[fish])[1] == True: addFish += 1
            #newFishID = len(fishDict.keys()) + 1
         #   fishDict[len(fishDict.keys()) + 1] = 8
    #if addFish > 0:



    #print("After Day " + str(day) + " : " + str(len(fishDict.keys())))

    printString = ""
    for fish in fishDict.keys(): printString += str(fishDict[fish]) + ", "
    print("After Day " + str(day) + " : " + printString)


print(len(fishDict.keys()))
