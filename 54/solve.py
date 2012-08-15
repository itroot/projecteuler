#!/usr/bin/env python
# -*- coding: utf-8 -*-


def generateLetter2Suit():
    suits=["Spades", "Hearts", "Diamonds", "Clubs"]
    result={}
    for suit in suits:
        result[suit[0]]=suit
    return result

letter2suit=generateLetter2Suit()


def generateLetter2Rank():
    lettersSmall=map(lambda e: chr(e), range(ord("2"), ord("9")+1))
    lettersBig=["T", "J", "Q", "K", "A"]
    letters=lettersSmall+lettersBig
    result={}
    for (i, letter) in enumerate(letters):
        result[letter]=i+2
    return result

letter2rank=generateLetter2Rank()

def generateCombination2Rank():
    combinationNames=[
      "HighCard"
    , "OnePair"
    , "TwoPairs"
    , "ThreeOfAKind"
    , "Straight"
    , "Flush"
    , "FullHouse"
    , "FourOfAKind"
    , "StraightFlush"
    , "RoyalFlush"
    ]
    result={}
    for (i, combinationName) in enumerate(combinationNames):
        result[combinationName]=i
    return result

combination2rank=generateCombination2Rank()

#print letter2suit
#print letter2rank
#print combination2rank

class Card:
    def __init__(self, abbreviation):
        self.__abbreviation=abbreviation
        self.__rank=letter2rank[abbreviation[0]]
        self.__suit=letter2suit[abbreviation[1]]
    def rank(self):
        return self.__rank
    def suit(self):
        return self.__suit
    def __repr__(self):
        return self.__abbreviation


def isFlush(cards):
    suitSet=set(map(lambda e: e.suit(), cards))
    return 1==len(suitSet)


class PokerGame:
    def __init__(self, gameLine):
        cardsLetters=gameLine.rstrip("\n\r").split(" ")
        self.__player1Cards=map(lambda e: Card(e), cardsLetters[0:5])
        self.__player2Cards=map(lambda e: Card(e), cardsLetters[5:])
        if isFlush(self.__player2Cards):
            print self.__player2Cards
    def classifyCombination(cards):
        pass
    def determineWinnerName(self):
        return "Friendship"

player1WinsTotal=0
for line in open("poker.txt").readlines():
    pokerGame=PokerGame(line);
    if ("Player1"==pokerGame.determineWinnerName()):
        player1WinsTotal+=1
print player1WinsTotal
