#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
import pprint
import Dijkstra

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


matrix=Dijkstra.loadMatrix("matrix.txt")
graph=convertMatrixToGraph(matrix)
lastIndex=len(matrix)-1
result=Dijkstra.shortestPath(graph, (0, 0), (lastIndex, lastIndex), matrix[0][0])
(distance, path)=result
pprint.pprint(distance)
