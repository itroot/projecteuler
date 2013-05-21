#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readSudoku(lines):
    dataLines=lines[1:]
    return map(lambda line: map(lambda digit: int(digit), line), dataLines)

def readSudokuFile(filename):
    result=[]
    lines=open(filename).read().rstrip("\n").split("\n")
    if (len(lines)%10!=0):
        raise Exception("Wrong file format: %d" % filename)
    for i in range(0, len(lines)/10):
        sudoku=readSudoku(lines[10*i:10*(i+1)])
        result.append(sudoku)
    return result

"""
def findEmptyPosition(sudoku):
    for (y, row) in enumerate(sudoku):
        for (x, digit) in enumerate(row):
            if digit==0:
                return (x, y)
    return None
"""

def getSquareDigits(sudoku, position):
    (xOrigin, yOrigin)=position
    x=(xOrigin/3)*3
    y=(yOrigin/3)*3
    squareSize=3
    squareRange=range(0, squareSize)
    result=[]
    for yRange in squareRange:
        for xRange in squareRange:
            result.append(sudoku[y+yRange][x+xRange])
    return result

def getUsedDigits(sudoku, position):
    (x, y)=position
    yDigits=sudoku[y]
    xDigits=map(lambda row: row[x], sudoku)
    squareDigits=getSquareDigits(sudoku, position)
    #print "xDigits", xDigits
    #print "yDigits", yDigits
    #print "squareDigits", squareDigits
    return set(xDigits+yDigits+squareDigits)-set([0])


def solveSudoku(sudoku):
    # on every 0 insert possible digit and continue
    #import pprint
    #pprint.pprint(sudoku)
    #position=findEmptyPosition(sudoku)
    stats=[]
    for (y, row) in enumerate(sudoku):
        for (x, digit) in enumerate(row):
            if digit==0:
                stats.append(((x, y), getUsedDigits(sudoku, (x, y))))
    if len(stats)==0:
        return sudoku
    stats=sorted(stats, reverse=True, key=lambda e: len(e[1]))
    #print stats[0]
    (position, digitSet)=stats[0]
    remainingDigits=set(range(1, 10))-digitSet
    if len(remainingDigits)==0:
        return None
    #if len(remainingDigits)!=1:
    #    raise Exception("Not implemented yet")
    for digit in remainingDigits:
        import copy
        (x, y)=position
        sudoku[y][x]=digit
        solvedSudoku=solveSudoku(copy.deepcopy(sudoku))
        if None!=solvedSudoku:
            return solvedSudoku
    return None
    #usedDigits=getUsedDigits(sudoku, position)
    #print usedDigits
    #(x, y)=position
    #print (x, y)

sudokuList=readSudokuFile("sudoku.txt")


solvedSudokuList=map(solveSudoku, sudokuList)
print reduce(lambda a, b : a+int("".join(map(str, b[0][:3]))), solvedSudokuList, 0)
