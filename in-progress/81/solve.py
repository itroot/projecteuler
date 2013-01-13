#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from collections import defaultdict

def loadMatrix(fileName):
    data=open(fileName).read()
    return map(lambda e: map(lambda e: int(e), e.split(",")), data.strip("\n").split("\n"))

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
        adjacencyListMap[source].append((sink, weight))
    #print adjacencyListMap
    verticeToDistance={}
    verticeSet=set(vertices)
    for vertice in vertices:
        verticeToDistance[vertice]=0 if vertice==startVertice else float("inf")
    while not 0==len(verticeSet):
        vertice=min(verticeSet, key=lambda e: verticeToDistance[e])
        distance=verticeToDistance[vertice]
        adjacentVerticeList=adjacencyListMap[vertice]
        for (adjacentVertice, weight) in adjacentVerticeList:
            adjacentDistance=verticeToDistance[adjacentVertice]
            possibleDistance=distance+weight
            if (possibleDistance<adjacentDistance):
                verticeToDistance[adjacentVertice]=possibleDistance
        verticeSet.remove(vertice)
    #print verticeToDistance
    return verticeToDistance[endVertice]

matrix=loadMatrix("matrix-test.txt")
graph=convertMatrixToGraph(matrix)
lastIndex=len(matrix)-1
distance=shortestPath(graph, (0, 0), (lastIndex, lastIndex))
pprint.pprint(distance+matrix[0][0])
