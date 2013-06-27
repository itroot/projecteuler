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

def parseCombination(combination):
    getRankList = lambda combination: map(lambda e: letter2RankIndex[e[0]], combination)
    def parseHighCard(combination):
        return max(getRankList(combination))
    def parseRoyalFlush(combination):
        if getRankList(higherRankList) == sorted(getRankList(combination)):
            return True
        else:
            return None
    parsers=[parseHighCard, parseRoyalFlush]
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
