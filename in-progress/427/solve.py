#!/usr/bin/env python
# -*- coding: utf-8 -*-

# see http://oeis.org/A055897 n*(n-1)^(n-1)
# see http://oeis.org/A228154 - little cheat

from collections import defaultdict

def f(numberList):
    d = []
    for number in numberList:
        if (len(d) == 0 or d[-1][0] != number):
            d.append([number, 1])
        else:
            d[-1][1] = d[-1][1] + 1
    return max(d, key=lambda e: e[1])[1]

print f([1, 1, 1])

def generate(n, k):
    if n == 0:
        return [[]]
    result = []
    for i in range(1, k+1):
        for g in generate(n-1, k):
            result.append([i]+g)
    return result

def g(n):
    return generate(n, n)

def x(n):
    data=g(n)
    datamap=[]
    dd = defaultdict(lambda:0)
    for d in data:
        result = f(d)
        datamap.append((d, result))
        dd[result] += 1
    import pprint
    l = list(dd.iteritems())
    print sum(map(lambda e: e[0]*e[1], l))
    print l
    open("test.txt", "a").write("\t".join(map(lambda e: str(e[1]), l))+"\n")
    l = map(lambda e: e[1]/n, l)
    x = map(lambda e: e/((n-1)*1.0), l[:-1])
    pprint.pprint(l)
    print x

for n in range(1, 9):
    print "====", n
    x(n)