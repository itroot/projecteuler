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

def classifyHighCard(cards):
    return tuple(["HighCard"]+sorted(map(lambda e: e.rank(), cards), reverse=True))

def findPairIndexInCards(cards):
    for i in range(0, len(cards)):
        for j in range(i+1, len(cards)):
            if (cards[i].rank()==cards[j].rank()):
                return (i, j)

def classifyOnePair(cards):
    pairIndexes=findPairIndexInCards(cards)
    if pairIndexes:
        otherCards=[]
        for (i, card) in enumerate(cards):
            if not i in pairIndexes:
                otherCards.append(card)
        return ["OnePair", cards[pairIndexes[0]].rank()]+sorted(map(lambda e: e.rank(), otherCards), reverse=True)
    else:
        return (None, None)

def classifyTwoPairs(cards):
    pairIndexes=findPairIndexInCards(cards)
    if pairIndexes:
        otherCards=[]
        for (i, card) in enumerate(cards):
            if not i in pairIndexes:
                otherCards.append(card)
        otherPairIndexes=findPairIndexInCards(otherCards)
        if otherPairIndexes:
            remainingCardRank=None
            for (i, card) in enumerate(otherCards):
                if not i in otherPairIndexes:
                    remainingCardRank=card.rank()
            return ["TwoPairs"]+sorted([cards[pairIndexes[0]].rank(), otherCards[otherPairIndexes[0]].rank()], reverse=True)+[remainingCardRank]
    return (None, None)
        
        

def classifyFlush(cards):
    suitSet=set(map(lambda e: e.suit(), cards))
    if (1==len(suitSet)):
        return ("Flush", cards[0].rank())
    else:
        return (None, None)


class PokerGame:
    def __init__(self, gameLine):
        cardsLetters=gameLine.rstrip("\n\r").split(" ")
        self.__player1Cards=map(lambda e: Card(e), cardsLetters[0:5])
        self.__player2Cards=map(lambda e: Card(e), cardsLetters[5:])
        if classifyFlush(self.__player2Cards)[0]:
            print self.__player2Cards
            print classifyHighCard(self.__player2Cards)
#        onePair=classifyOnePair(self.__player2Cards)
#        if (onePair[0]):
#            print onePair
        twoPairs=classifyTwoPairs(self.__player2Cards)
        if (twoPairs[0]):
            print twoPairs, self.__player2Cards
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
