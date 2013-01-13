#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
import pprint
import Dijkstra

matrix=Dijkstra.loadMatrix("matrix.txt")
graph=Dijkstra.convertMatrixToGraph(matrix, up=True, left=False)
(vertices, edges)=graph
vertices.extend(["begin", "end"])
lastIndex=len(matrix)-1
for i in range(0, len(matrix)):
    edges.append(("begin", (i, 0), matrix[i][0]))
    edges.append(((i, lastIndex), "end", 0))
newGraph=(vertices, edges)
result=Dijkstra.shortestPath(newGraph, "begin", "end", 0)
(distance, path)=result
pprint.pprint(distance)
