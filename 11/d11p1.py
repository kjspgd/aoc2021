#!/usr/local/bin/python3
lineList = []
debug = 0
octoDict = {}
flashCount = 0

def incrementone():
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],int):
                octoDict[row][column] += 1
    return True

def render():
    print("----------")
    for row in octoDict.keys():
        renderStr = ''
        renderStr = "".join(map(str, octoDict[row].values()))
        print(renderStr)
    print("----------")
    return True


def updateAdjacent():
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],str):
                if octoDict[row][column]=='f':
                    #if octoDict.has_key(row-1):
                    if (row-1) in octoDict.keys():
                        if (column-1) in octoDict[row-1].keys():
                            if isinstance(octoDict[row-1][column-1],int): octoDict[row-1][column-1] += 1
                        if (column) in octoDict[row-1].keys():
                            if isinstance(octoDict[row-1][column],int): octoDict[row-1][column] += 1
                        if (column+1) in octoDict[row-1].keys():
                            if isinstance(octoDict[row-1][column+1],int): octoDict[row-1][column+1] += 1
                    if (row) in octoDict.keys():
                        if (column-1) in octoDict[row].keys():
                            if isinstance(octoDict[row][column-1],int): octoDict[row][column-1] += 1
                        if (column+1) in octoDict[row].keys():
                            if isinstance(octoDict[row][column+1],int): octoDict[row][column+1] += 1
                    if (row+1) in octoDict.keys():
                        if (column-1) in octoDict[row+1].keys():
                            if isinstance(octoDict[row+1][column-1],int): octoDict[row+1][column-1] += 1
                        if (column) in octoDict[row+1].keys():
                            if isinstance(octoDict[row+1][column],int): octoDict[row+1][column] += 1
                        if (column+1) in octoDict[row+1].keys():
                            if isinstance(octoDict[row+1][column+1],int): octoDict[row+1][column+1] += 1

    return True


def flashesExits():
    state = False
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],str):
                if octoDict[row][column]=='f': state = True
    return state

def setFlashes():
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],int):
                    if octoDict[row][column] >9:
                        octoDict[row][column]='f'
                #print("Flash at "+ str(row)+","+str(column)+" - "+str(octoDict[row][column]))
    return True

def shiftFlashes():
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],str):
                if octoDict[row][column]=='f':
                    octoDict[row][column]='g'
            #print("Flash at "+ str(row)+","+str(column)+" - "+str(octoDict[row][column]))
    return True

def zeroFlashes():
    passCount = 0
    for row in octoDict.keys():
        for column in octoDict[row].keys():
            if isinstance(octoDict[row][column],str):
                #if octoDict[row][column]=='f':
                    octoDict[row][column]=0
                    passCount +=1
            #print("Flash at "+ str(row)+","+str(column)+" - "+str(octoDict[row][column]))
    return passCount

for line in open("sample_input.txt"):
    lineList.append(line.rstrip())

#Init the two dimensional dict
for row in range(0,len(lineList)):
    octoDict[row] = {}
    for column in range(0,len(str(lineList[row]))):
        octoDict[row][column]=int(lineList[row][column])

#print(octoDict)
#setFlashes()
if debug: render()
for step in range(0,100):
    if debug: print("Step "+str(step))
    incrementone()
    setFlashes()
    #then loop here
    while flashesExits():
        if debug: print("Inside Loop")
        #do adjacency work
        updateAdjacent()
        #shift f's to gs
        shiftFlashes()
        if debug: render()
        #input()
        #shift 9s to f
        setFlashes()
    setFlashes()


    if debug: print("Flashes no longer exist")
    flashCount += zeroFlashes()
    if debug: render()




print(flashCount)