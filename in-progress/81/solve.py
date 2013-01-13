#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from collections import defaultdict
import heapq # avoid changing old entries

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

def shortestPath(graph, startVertice, endVertice, startWeight):
    (vertices, edges)=graph
    adjacencyListMap=defaultdict(list)
    for edge in edges:
        (source, sink, weight)=edge
        adjacencyListMap[source].append((sink, weight))
    #print adjacencyListMap
    verticeToDistance={}
    heap=[]
    verticeSet=set(vertices)
    for vertice in vertices:
        distance=0 if vertice==startVertice else float("inf")
        verticeToDistance[vertice]=distance
        heapq.heappush(heap, (distance, vertice))
    while not 0==len(verticeSet):
        (_, vertice)=heapq.heappop(heap)
        if not vertice in verticeSet:
            continue
        distance=verticeToDistance[vertice]
        adjacentVerticeList=adjacencyListMap[vertice]
        for (adjacentVertice, weight) in adjacentVerticeList:
            adjacentDistance=verticeToDistance[adjacentVertice]
            possibleDistance=distance+weight
            if (possibleDistance<adjacentDistance):
                verticeToDistance[adjacentVertice]=possibleDistance
                heapq.heappush(heap, (possibleDistance, adjacentVertice))
        verticeSet.remove(vertice)
    #print verticeToDistance
    return verticeToDistance[endVertice]+startWeight

matrix=loadMatrix("matrix.txt")
graph=convertMatrixToGraph(matrix)
lastIndex=len(matrix)-1
distance=shortestPath(graph, (0, 0), (lastIndex, lastIndex), matrix[0][0])
pprint.pprint(distance)
