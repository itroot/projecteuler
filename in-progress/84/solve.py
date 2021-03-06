#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.codeproject.com/Articles/36025/Markov-Monopoly
"""

import numpy
import pprint
import math

def saveMatrix(matrix, name):
    numpy.savetxt("%s.csv"%name, numpy.asarray(matrix), delimiter=",")

boardSize = 40

rollMatrix = numpy.matrix([[0.0]*boardSize]*boardSize)
for i in range(0, boardSize):
    for j in range(2, 12+1):
        value = (6 - math.fabs(7-j))
        #print value
        rollMatrix[(i+j)%boardSize, i] = value/36.0
    #break

#print rollMatrix
saveMatrix(rollMatrix, "rollMatrix")

stateMatrix = numpy.matrix([[0.0]*boardSize]*boardSize)
for i in range(0, boardSize):
    stateMatrix[i, i] = 1.0
stateMatrix[10, 30] = 0.0
stateMatrix[10, 30] = 1.0
for i in range(0, boardSize):
    if i in (2, 17, 33):
        stateMatrix[0, i] = 1.0/16.0
        stateMatrix[10, i] = 1.0/16.0
        stateMatrix[i, i] = 14.0/16.0
saveMatrix(stateMatrix, "stateMatrix")
resultMatrix = stateMatrix*rollMatrix
saveMatrix(resultMatrix, "resultMatrix")
print numpy.linalg.eigvals(resultMatrix)
"""
Below is old solution
"""
import sys
sys.exit(0)

board=[
"GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
"JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
"FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
"G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2",
]
length=len(board)

timesVisited=[0]*length
timesVisited[0]=1

def rollTheDice():
    import random
    return random.randrange(6)+1

def rollTheDiceTwice():
    return (rollTheDice(), rollTheDice())

communityChestCardPile=["2GO", "2JAIL"]+(14*["DONTMOVE"])
chanceCardPile=["2GO", "2JAIL", "2C1", "2E3", "2H2", "2R1", "2nR", "2nR", "2nU", "back3"]+(6*["DONTMOVE"])

communityChestActions={
    "2JAIL" : (lambda position: 10),
    "2GO" : (lambda position: 0),
    "DONTMOVE" : (lambda position: position),
}

def moveToNext(position, sortedPointList):
    for point in sortedPointList:
        if position<point:
            return point
    return sortedPointList[0]

chanceActions={
    "2JAIL" : (lambda position: 10),
    "2GO" : (lambda position: 0),
    "2C1" : (lambda position: 11),
    "2E3" : (lambda position: 24),
    "2H2" : (lambda position: 39),
    "2R1" : (lambda position: 5),
    "2nR" : (lambda position: moveToNext(position, (5, 15, 25, 35))),
    "2nU" : (lambda position: moveToNext(position, (12, 18))),
    "back3" : (lambda position: (position-3+length)%length),
    "DONTMOVE" : (lambda position: position),
}

# http://stackoverflow.com/questions/473973/shuffle-an-array-with-python
def getRandomCardFromPile(pile):
    import random
    number=random.randrange(0, len(pile))
    return pile[number]

class GameState:
    position=0
    lastDoubleCount=0
    def makeMove(self):
        (dice1, dice2)=rollTheDiceTwice()
        if (dice1==dice2):
            self.lastDoubleCount+=1
        else:
            self.lastDoubleCount=0
        if self.lastDoubleCount==3:
            self.lastDoubleCount=0
            self.position=10
        else:
            diceSum=dice1+dice2
            self.position=(self.position+diceSum)%length
            label=board[self.position]
            if (label.startswith("CC")):
                communityChestCard=getRandomCardFromPile(communityChestCardPile)
                self.position=communityChestActions[communityChestCard](self.position)
            elif (label.startswith("CH")):
                chanceCard=getRandomCardFromPile(chanceCardPile)
                self.position=chanceActions[chanceCard](self.position)
            if (label=="G2J"):
                self.position=10
        timesVisited[self.position]+=1

experimentNumber=10**5
gameState=GameState()

for i in range(0, experimentNumber):
    gameState.makeMove()
print sorted(zip(board, timesVisited), key=lambda e: e[1], reverse=True)[:5]
