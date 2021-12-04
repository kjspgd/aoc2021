#!/usr/local/bin/python3
newgame = 0
bingoNumbers = []
linecount = 1
gameArray = []
game = []
continueGame = 1
winningResult = 0
longestGame = 0
debug = 0

def addColumns(incGame):
    returnVal = []
    workingArray = incGame.copy()
    for i in range(0,5):
        newSolution = []
        for solution in incGame:
            newSolution.append(solution[i])
        workingArray.append(newSolution)
    return workingArray



for line in open("input.txt"):
    if linecount==1:
        bingoNumbers=list(map(int, line.rstrip().split(",")))
    else:
        if len(line.rstrip())==0:
            if(len(game)>0):
                gameArray.append(addColumns(game))
            game=[]
        else:
            game.append((list(map(int, line.rstrip().split()))))
            newgame=0
    linecount += 1


for theGame in gameArray:
    if debug: print("Start game")
    continueGame = 1
    for i in range(4,len(bingoNumbers)):
             checkList = bingoNumbers[0:i]
             for solution in theGame:
                 if continueGame:
                     if len(list(set(checkList) & set(solution)))==5:
                         if debug:
                            print("-----------------------------------------")
                            print("Winner with " + str(checkList[-1]))
                            print("Winner at char " + str(i))
                            print("Winning Numbers: " + str(checkList))
                         winningBoard = []
                         for j in range (0,5):
                            winningBoard += (theGame[j])
                         if i>longestGame:
                            longestGame=i
                            winningResult= sum(list(set(winningBoard) - set(checkList)))* checkList[-1]
                         if debug:
                            print(winningBoard)
                            print(sum(list(set(winningBoard) - set(checkList))))
                            print(sum(list(set(winningBoard) - set(checkList)))* checkList[-1])
                            print("-----------------------------------------")
                         #print(solution)
                         #quit()
                         continueGame = 0




print("------------Winning Result---------------")
print(winningResult)
print("-----------------------------------------")
