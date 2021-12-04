#!/usr/local/bin/python3
import numpy as nmp
import csv
newgame = 0
bingoNumbers = []
linecount = 1
gameDict = {}
gameNumber = 1
gameArray = []
chxDinner = 0
winners = []

def addColumns(incGame):
    returnVal = []
    workingArray = incGame.copy()
    #print("addColumns incomingGame is " + str(incGame))
    for i in range(0,5):
        newSolution = []
        for solution in incGame:
            newSolution.append(solution[i])
        workingArray.append(newSolution)
    return workingArray


def checkGame(incGame, incNumList):
    returnVal = []
    gameSum = 0
    for game in range(0,5):
        gameSum += sum(game[i])
    print("Gamesum: " + str(gameSum))

    for i in range(4,len(incNumList)):
        checkList = incNumList[0:i]

        for solution in incGame:
            print("---Testing----")
            print(checkList)
            print(solution)
            print(len(list(set(checkList) & set(solution))))
            print("-------")
            if len(list(set(checkList) & set(solution))) == 5:
                returnVal = [solution, i]
                print("Winner with " + str(solution))
                break



    return returnVal

game = []
for line in open("sample_input.txt"):
    if linecount==1:
        bingoNumbers=list(map(int, line.rstrip().split(",")))
    else:
        if len(line.rstrip())==0:
            #print("Winner! " + str(checkGame(gameArray, bingoNumbers)))
            #newgame=1
            #linecount=0
            if(len(game)>0):
                gameArray.append(addColumns(game))
            game=[]

        else:
            game.append((list(map(int, line.rstrip().split()))))
            newgame=0
    linecount += 1


for i in range(4,len(bingoNumbers)):
     checkList = bingoNumbers[0:i]
     for theGame in gameArray:
         for solution in theGame:
             if len(list(set(checkList) & set(solution)))==5:
                print("Winner with " + str(checkList[-1]))
                print("Winning Numbers: " + str(checkList))
                winningBoard = []
                for j in range (0,5):
                    winningBoard += (theGame[j])
                print(winningBoard)
                print(sum(list(set(winningBoard) - set(checkList))))
                print(sum(list(set(winningBoard) - set(checkList)))* checkList[-1])
                #print(solution)
                quit()
#print(gameArray)

#print(bingoNumbers)


