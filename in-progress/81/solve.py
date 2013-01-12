#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

def loadMatrix(fileName):
    data=open(fileName).read()
    return map(lambda e: e.split(" "), data.strip("\n").split("\n"))

def convertMatrixToGraph(matrix, down=True, right=True):
    vertices=[]
    edges=[]
    dimension=len(matrix)
    for i in range(0, dimension):
        for j in range(0, dimension):
            vertices.append((i, j))
            if (down and i+1<dimension):
                edges.append(((i, j), (i+1, j), matrix[i+1][j]))
            if (right and j+1<dimension):
                edges.append(((i, j), (i, j+1), matrix[i][j+1]))
    return (vertices, edges)

matrix=loadMatrix("matrix-test.txt")
graph=convertMatrixToGraph(matrix)
pprint.pprint(graph)
