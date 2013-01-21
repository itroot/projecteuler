#!/usr/bin/env python
# -*- coding: utf-8 -*-

board=[
"GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
"JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
"FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
"G2J", "G1", "G2", "GC3", "G3", "R4", "CH3", "H1", "T2", "H2", 
]

timesVisited=[0 for i in range(0, len(board))]

def rollTheDice():
    import random
    return random.randrange(6)+1

def rollTheDiceTwice():
    return (rollTheDice(), rollTheDice())

class GameState:
    position=0
    lastDoubleCount=0
    def makeMove(self):
        (dice1, dice2)=rollTheDiceTwice()
        if (dice1==dice2):
            lastDoubleCount+=1
        else:
            lastDoubleCount=0
        if lastDoubleCount==3:
            lastDoubleCount=0
            position=10
            

experimentNumber=10#10**6
gameState=GameState()

for i in range(0, experimentNumber):
    gameState.makeMove()
