#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from collections import defaultdict

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

def shortestPath(graph, startVertice, endVertice):
    (vertices, edges)=graph
    adjacencyListMap=defaultdict(list)
    for edge in edges:
        (source, sink, weight)=edge
        adjacencyListMap[source].append(sink)
    print adjacencyListMap

matrix=loadMatrix("matrix-test.txt")
graph=convertMatrixToGraph(matrix)
lastIndex=len(matrix)-1
path=shortestPath(graph, (0, 0), (lastIndex, lastIndex))
pprint.pprint(path)
