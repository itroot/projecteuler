#!/usr/bin/env python
# -*- coding: utf-8 -*-

suitList = ["S", "H", "D", "C"]
higherRankList = ["T", "J", "Q", "K", "A"]
rankList = map(str, range(2, 10)) + higherRankList
letter2RankIndex = dict(map(lambda (index, value): (value, index), enumerate(rankList)))

print "Suits:", suitList
print "Ranks:", rankList
print "Letter2RankIndex:", letter2RankIndex

def readGameListFromFile(name):
    def splitLine(line):
        sequence = line.split(" ")
        return (sequence[:5], sequence[5:])
    lines = open(name).read().rstrip("\r\n").split("\r\n")
    games = map(splitLine, lines)
    return games

#(rank, card, highest, next highest)
def parseCombination(combination):
    getRankList = lambda combination: map(lambda e: letter2RankIndex[e[0]], combination)
    getSuitSet = lambda combination: set(map(lambda e: e[1], combination))
    def getRankToCardList(combination):
            from collections import defaultdict
            result = defaultdict(list)
            for card in combination:
                result[card[0]].append(card)
            return dict(result)
    def getSortedRankTupleList(combination):
        return sorted(list(getRankToCardList(combination).iteritems()), key=lambda e: len(e[1]))
    def helpParseHouseAndFour(combination, number):
        rankToCardList = getSortedRankTupleList(combination)
        if len(rankToCardList) == 2:
            if (len(rankToCardList[1][1]) == number):
                return (rankToCardList[1][0], rankToCardList[0][0])
        return None
    def parseHighCard(combination):
        return max(getRankList(combination))
    def parseOnePair(combination):
        pass
    def parseTwoPairs(combination):
        pass
    def parseThreeOfAKind(combination):
        rankToCardList = getSortedRankTupleList(combination)
        if (len(rankToCardList[2][1]) == 3):
            tail = sorted(map(lambda e: e[0], rankToCardList[:2]), key = lambda e: letter2RankIndex[e], reverse = True)
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
            royalFlashSmallestRank = letter2RankIndex["T"]
            if straightResult[0] == royalFlashSmallestRank:
                return royalFlashSmallestRank
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
        result = parser(combination)
        #print result
        if None != result:
            return (index, result)
    return None

def isPlayerOneWin(game):
    return parseCombination(game[0]) > parseCombination(game[1])

gameList = readGameListFromFile("poker.txt")
playerOneWinNumber = 0
for game in gameList:
    #print game
    if isPlayerOneWin(game):
        playerOneWinNumber += 1
print playerOneWinNumber
