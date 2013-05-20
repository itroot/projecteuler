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

def solveSudoku(sudoku):
    # on every 0 insert possible digit and continue
    print sudoku

sudokuList=readSudokuFile("sudoku.txt")

for sudoku in sudokuList:
    solveSudoku(sudoku) 
