#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../lib")
import pprint
import Dijkstra

matrix=Dijkstra.loadMatrix("matrix.txt")
graph=Dijkstra.convertMatrixToGraph(matrix, up=True, left=True)
lastIndex=len(matrix)-1
result=Dijkstra.shortestPath(graph, (0, 0), (lastIndex, lastIndex), matrix[0][0])
(distance, path)=result
pprint.pprint(distance)
