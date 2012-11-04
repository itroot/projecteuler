# -*- coding: utf-8 -*-

def generateLetter2Suit():
    suits=["Spades", "Hearts", "Diamonds", "Clubs"]
    result={}
    for suit in suits:
        result[suit[0]]=suit
    return result

def generateLetter2Rank():
    lettersSmall=map(lambda e: chr(e), range(ord("2"), ord("9")+1))
    lettersBig=["T", "J", "Q", "K", "A"]
    letters=lettersSmall+lettersBig
    result={}
    for (i, letter) in enumerate(letters):
        result[letter]=i+2
    return result

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

def findPairIndexInCards(cards):
    for i in range(0, len(cards)):
        for j in range(i+1, len(cards)):
            if (cards[i].rank()==cards[j].rank()):
                return (i, j)

