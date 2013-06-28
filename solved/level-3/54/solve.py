#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

suitList = ["S", "H", "D", "C"]
higherRankList = ["T", "J", "Q", "K", "A"]
rankList = map(str, range(2, 10)) + higherRankList
letter2RankIndex = dict(map(lambda (index, value): (value, index), enumerate(rankList)))

def convertRank(stringRank):
    return letter2RankIndex[stringRank]

def parseCard(card):
    from collections import namedtuple
    return namedtuple("Card", ["rank", "suit"])(convertRank(card[0]), card[1])

#print "Suits:", suitList
#print "Ranks:", rankList
#print "Letter2RankIndex:", letter2RankIndex

def readGameListFromFile(name):
    def splitLine(line):
        sequence = map(parseCard, line.split(" "))
        return (sequence[:5], sequence[5:])
    lines = open(name).read().rstrip("\r\n").split("\r\n")
    games = map(splitLine, lines)
    return games

#(rank, card, highest, next highest)
def parseCombination(combination):
    getRankList = lambda combination: map(lambda e: e.rank, combination)
    getSuitSet = lambda combination: set(map(lambda e: e.suit, combination))
    def getRankToCardList(combination):
            from collections import defaultdict
            result = defaultdict(list)
            for card in combination:
                result[card.rank].append(card)
            return dict(result)
    def getSortedRankTupleList(combination):
        return sorted(list(getRankToCardList(combination).iteritems()), key=lambda e: len(e[1]))
    def helpParseHouseAndFour(combination, number):
        rankToCardList = getSortedRankTupleList(combination)
        if len(rankToCardList) == 2:
            if (len(rankToCardList[1][1]) == number):
                return (rankToCardList[1][0], rankToCardList[0][0])
        return None
    sortRankTupleList = lambda rankList: sorted(map(lambda e: e[0], rankList), reverse = True)
    def parseHighCard(combination):
        return (max(getRankList(combination)),)
    def parseOnePair(combination):
        rankToCardList = getSortedRankTupleList(combination)
        if len(rankToCardList[3][1]) == 2:
            tail = sortRankTupleList(rankToCardList[:3])
            return (rankToCardList[3][0], tail[0], tail[1], tail[2])
    def parseTwoPairs(combination):
        rankToCardList = getSortedRankTupleList(combination)
        if len(rankToCardList[2][1]) == 2 and len(rankToCardList[1][1]) == 2:
            tail = sortRankTupleList(rankToCardList[1:])
            return (tail[0], rankToCardList[0][0])
    def parseThreeOfAKind(combination):
        rankToCardList = getSortedRankTupleList(combination)
        if (len(rankToCardList[2][1]) == 3):
            tail = sortRankTupleList(rankToCardList[:2])
            return (rankToCardList[2][0], tail[0], tail[1])
    def parseStraight(combination):
        rankList = sorted(getRankList(combination))
        smallestRank = rankList[0]
        if (rankList == range(smallestRank, smallestRank+5)):
            return (smallestRank,)
    def parseFlush(combination):
        if len(getSuitSet(combination)) == 1:
            return parseHighCard(combination)
        return None
    def parseFullHouse(combination):
        return helpParseHouseAndFour(combination, 3)
    def parseFourOfAKind(combination):
        return helpParseHouseAndFour(combination, 4)
    def parseStraightFlush(combination):
        flushResult = parseFlush(combination)
        if (not flushResult is None):
            return parseStraight(combination)
        return None
    def parseRoyalFlush(combination):
        straightResult = parseStraightFlush(combination)
        if not straightResult is None:
            if straightResult[0] == letter2RankIndex["T"]:
                return straightResult
        return None
    parsers=[
        parseHighCard,
        parseOnePair,
        parseTwoPairs,
        parseThreeOfAKind,
        parseStraight,
        parseFlush,
        parseFullHouse,
        parseFourOfAKind,
        parseStraightFlush,
        parseRoyalFlush,
    ]
    for (index, parser) in reversed(list(enumerate(parsers))):
        combinationResult = parser(combination)
        if None != combinationResult:
            result = (index, combinationResult)
            #print result
            return result
    raise Exception("Can't be here")

def isPlayerOneWin(game):
    return parseCombination(game[0]) > parseCombination(game[1])

gameList = readGameListFromFile("poker.txt")
playerOneWinNumber = 0
for game in gameList:
    #print game
    if isPlayerOneWin(game):
        playerOneWinNumber += 1
print playerOneWinNumber
