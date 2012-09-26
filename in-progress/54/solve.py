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

#print letter2rank

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

#TODO use another classifications
def splitByRank(cards):
    result={}
    for (i, card) in enumerate(cards):
        rank=card.rank()
        if not rank in result:
            result[rank]=[]
        result[rank].append(i)
    return result

def classifyThreeOfAKind(cards):
    rankToCardIdList=splitByRank(cards)
    threeId=None
    for (rank, cardIdList) in rankToCardIdList.iteritems():
        if 3==len(cardIdList):
            threeId=cardIdList
    if None==threeId:
        return (None, None)
    else:
        lastIdList=list(set(range(0, 5)).difference(set(threeId)))
        lastCards=map(lambda e: cards[e].rank(), lastIdList)
        sortedLastCards=sorted(lastCards, reverse=True)
        return ("ThreeOfAKind", cards[threeId[0]].rank(), sortedLastCards)

def classifyStraight(cards):
    cardRankList=map(lambda e: e.rank(), cards)
    sortedRankList=sorted(cardRankList)
    startRank=sortedRankList[0]
    stopRank=startRank+5
    if range(startRank, stopRank)==sortedRankList:
        #print sortedRankList, cardRankList, cards
        return ("Straight", [startRank])
    else:
        return (None, None)

#straightCards=map(lambda e: Card(e), ["2S", "3S", "4D", "5S", "6S"]
#print ">>>", classifyStraight(straightCards), straightCards

def classifyFlush(cards):
    suitSet=set(map(lambda e: e.suit(), cards))
    if (1==len(suitSet)):
        return ("Flush", cards[0].rank())
    else:
        return (None, None)

def classifyFullHouse(cards):
    threeOfAKind=classifyThreeOfAKind(cards)
    if (None!=threeOfAKind[0]):
        if (threeOfAKind[2][0]==threeOfAKind[2][1]):
            return("FullHouse", (threeOfAKind[2][0]))
        else:
            return (None, None)
    else:
        return (None, None)

def classifyFourOfAKind(cards):
    rankToCardIdList=splitByRank(cards)
    fourId=None
    for (rank, cardIdList) in rankToCardIdList.iteritems():
        if 4==len(cardIdList):
            fourId=cardIdList
    if None==fourId:
        return (None, None)
    lastId=list(set(range(0, 5)).difference(set(fourId)))[0]
    return ("FourOfAKind", cards[fourId[0]].rank(), cards[lastId].rank())

#fourOfAKind=map(lambda e: Card(e), ["2S", "2S", "2D", "2S", "6S"])
#print ">>>", classifyFourOfAKind(fourOfAKind), fourOfAKind

def classifyStraightFlush(cards):
    straight=classifyStraight(cards)
    flush=classifyFlush(cards)
    if None!=straight[0] and None!=flush[0]:
        return ("StraightFlush", straight[1])
    else:
        return (None, None)

def classifyRoyalFlush(cards):
    straightFlush=classifyStraightFlush(cards)
    if None!=straightFlush[0] and 10==straightFlush[0][1]:
        return ("RoyalFlush")
    else:
        return (None, None)

def classifyCombination(cards):
    pass

class PokerGame:
    def __init__(self, gameLine):
        cardsLetters=gameLine.rstrip("\n\r").split(" ")
        self.__player1Cards=map(lambda e: Card(e), cardsLetters[0:5])
        self.__player2Cards=map(lambda e: Card(e), cardsLetters[5:])
#        if classifyFlush(self.__player2Cards)[0]:
#            print self.__player2Cards
#            print classifyHighCard(self.__player2Cards)
#        onePair=classifyOnePair(self.__player2Cards)
#        if (onePair[0]):
#            print onePair
#        twoPairs=classifyTwoPairs(self.__player2Cards)
#        if (twoPairs[0]):
#            print twoPairs, self.__player2Cards
#        threeOfAKind=classifyThreeOfAKind(self.__player2Cards)
#        if (threeOfAKind[0]):
#            print threeOfAKind, self.__player2Cards
#        fullHouse=classifyFullHouse(self.__player2Cards)
#        if (fullHouse[0]):
#            print fullHouse, self.__player2Cards
        fourOfAKind=classifyFourOfAKind(self.__player1Cards)
        if (fourOfAKind[0]):
            print fourOfAKind, self.__player1Cards
#        straight=classifyStraight(self.__player2Cards)
#        if (straight[0]):
#            print straight, self.__player2Cards
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
