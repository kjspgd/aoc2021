#!/usr/local/bin/python3
count = 0
debug = 0
allLines = []
winList = []


def checkPoint(incRow, incColumn, allLines):
    #print(incx)
    #print(incy)
    returnVal = 0
    checkVal = int(allLines[incRow][incColumn])
    #if(incRow==0 or incRow==len(allLines)-1 or incColumn==0 or incColumn==len(allLines[incRow])-1):
    #NW Corner
    if((incRow==0 and incColumn==0)):
         if \
                 checkVal< allLines[incRow][incColumn+1] and \
                 checkVal< allLines[incRow+1][incColumn] and \
                 checkVal< allLines[incRow+1][incColumn+1]:
            returnVal = checkVal+1


    #NE Corner
    elif(incRow==0 and incColumn==len(allLines[incRow])-1):
        if \
                checkVal< allLines[incRow][incColumn-1] and \
                checkVal< allLines[incRow+1][incColumn-1] and \
                checkVal< allLines[incRow+1][incColumn]: \
            returnVal = checkVal+1



    #SW Corner
    elif(incRow==len(allLines)-1 and incRow==0):
        if \
                checkVal< allLines[incRow-1][incColumn] and \
                checkVal< allLines[incRow-1][incColumn+1] and \
                checkVal< allLines[incRow][incColumn+1]: \
            returnVal = checkVal+1




    #SE corner
    elif(incRow==len(allLines)-1 and incColumn==len(allLines[incRow])-1):
        if \
                checkVal< allLines[incRow-1][incColumn-1] and \
                checkVal< allLines[incRow-1][incColumn] and \
                checkVal< allLines[incRow][incColumn-1]: \
            returnVal = checkVal+1



    #Top row
    elif(incRow==0):
        if \
                        checkVal< allLines[incRow][incColumn-1] and \
                        checkVal< allLines[incRow][incColumn+1] and \
                        checkVal< allLines[incRow+1][incColumn-1] and \
                        checkVal< allLines[incRow+1][incColumn] and \
                        checkVal< allLines[incRow+1][incColumn+1]:
            returnVal = checkVal+1



    #bottom row
    elif(incRow==len(allLines)-1):
        if \
                checkVal< allLines[incRow-1][incColumn-1] and \
                        checkVal< allLines[incRow-1][incColumn] and \
                        checkVal< allLines[incRow-1][incColumn+1] and \
                        checkVal< allLines[incRow][incColumn-1] and \
                        checkVal< allLines[incRow][incColumn+1]:
            returnVal = checkVal+1
    #left edge
    elif(incColumn==0):
        if \
                        checkVal< allLines[incRow-1][incColumn] and \
                        checkVal< allLines[incRow-1][incColumn+1] and \
                        checkVal< allLines[incRow][incColumn+1] and \
                        checkVal< allLines[incRow+1][incColumn] and \
                        checkVal< allLines[incRow+1][incColumn+1]:
            returnVal = checkVal+1


    #right edge
    elif(incColumn==len(allLines[incRow])-1):
        if \
                checkVal< allLines[incRow-1][incColumn-1] and \
                        checkVal< allLines[incRow-1][incColumn] and \
                        checkVal< allLines[incRow][incColumn-1] and \
                        checkVal< allLines[incRow+1][incColumn-1] and \
                        checkVal< allLines[incRow+1][incColumn]:
            returnVal = checkVal+1



    #print("Skipping " + str(incRow) + "," + str(incColumn))
    #returnVal = -1

    else:

        print("Checking " + str(incRow) + "," + str(incColumn))
        if \
            checkVal< allLines[incRow-1][incColumn-1] and \
            checkVal< allLines[incRow-1][incColumn] and \
            checkVal< allLines[incRow-1][incColumn+1] and \
            checkVal< allLines[incRow][incColumn-1] and \
            checkVal< allLines[incRow][incColumn+1] and \
            checkVal< allLines[incRow+1][incColumn-1] and \
            checkVal< allLines[incRow+1][incColumn] and \
            checkVal< allLines[incRow+1][incColumn+1]:
                returnVal = checkVal+1
        else:
            returnVal = 0
    print(returnVal)
    return returnVal

for line in open("input.txt"):
    lineArray = []
    if debug: print(line)
    for item in (line.rstrip()):
        lineArray.append(int(item))
    allLines.append(lineArray)

for row in range(0,len(allLines)):
    for column in range(0,len(allLines[row])):
        #print(str(row) + str(column))
        #print(str(x)+","+str(y)+": "+allLines[y][x])
        winList.append(checkPoint(row, column, allLines))

print(winList)
print(sum(winList))
