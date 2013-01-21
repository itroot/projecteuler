#!/usr/bin/env python
# -*- coding: utf-8 -*-

board=[
"GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
"JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
"FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
"G2J", "G1", "G2", "GC3", "G3", "R4", "CH3", "H1", "T2", "H2", 
]
length=len(board)

timesVisited=[0 for i in range(0, length)]
# timesVisited[0]=1

def rollTheDice():
    import random
    return random.randrange(6)+1

def rollTheDiceTwice():
    return (rollTheDice(), rollTheDice())

def getCommunityChestCard():
    import random
    number=random.randrange(0, 16)
    if (0==number):
        return "2GO"
    elif (1==number):
        return "2JAIL"
    else:
        return None

def getChanceCard():
    import random
    cardList=["2GO", "2JAIL", "2C1", "2E3", "2H2", "2R1", "2nR", "2nR", "2nU", "back3"]
    number=random.randrange(0, 16)
    if number<len(cardList):
        return cardList[number]

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
            position=10
    position=(position+length)%length
    label=board[position]
    if (label=="G2J"):
        position=10
    elif (label.startswith("CC")):
        communityChestCard=getCommunityChestCard()
        if "2JAIL"==communityChestCard:
            position=10
        elif "2GO"==communityChestCard:
            position=0
    elif (label.startswith("CH")):
        pass
    timesVisited[position]+=1
            

experimentNumber=10#10**6
gameState=GameState()

for i in range(0, experimentNumber):
    gameState.makeMove()

print sorted(zip(board, timesVisited), key=lambda e: e[1], reverse=True)[:5]
