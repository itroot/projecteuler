#!/usr/bin/env python
# -*- coding: utf-8 -*-


attemptList=map(lambda e: list(str(e.rstrip("\n"))), open("keylog.txt").readlines())
#print attemptList

edges=[]

for attempt in attemptList:
    (first, second, third)=tuple(attempt)
    edges.append((first, second))
    edges.append((second, third))

def generateDotDigraph(edgeList):
    import subprocess
    convertToDotEntry=lambda (first, second): str(first)+" -> "+str(second)+" ;"
    dighraph="\n".join(["digraph G {"]+map(convertToDotEntry, edgeList)+["}"])
    processHandle=subprocess.Popen("dot -Gweight=0.5 -Tpng -o graph.png", shell=True, stdin=subprocess.PIPE)
    processHandle.stdin.write(dighraph)
    processHandle.stdin.close()
    processHandle.wait()

generateDotDigraph(edges)
