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

def hackySolution(edgeList):
    import collections
    result=[]
    while 0!=len(edgeList):
        allSet=set()
        referencedSet=set()
        for (first, second) in edgeList:
            allSet.add(first)
            allSet.add(first)
            referencedSet.add(second)
        independentSet=allSet.difference(referencedSet)
        result+=list(independentSet)
        tail=list(set(map(lambda e: e[1], edgeList)))
        edgeList=filter(lambda (first, second): not first in independentSet , edgeList)
    return result+tail

print "".join(hackySolution(edges))
