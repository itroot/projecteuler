#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

upperLimit = 15
upperLimit = 200

Way = namedtuple("Way", ["father", "mother", "steps"])
d = {1 : [Way(None, None, 0)]}

# gcd ?

def path(number):
    if 1 == number:
        return [1]
    else:
        way = d[number]
        father = way[0].father
        mother = way[0].mother
        return [number] + path(father) + path(mother)

def dijest(number):
    #print number
    result = []
    for s1 in range(1, number/2+1):
        s2 = number - s1
        # FIX this
        # FIXME TODO problem is that a = s1 + s2, s2>=s1. We need to optimize
        # by number of common numbers in s1 and s2. This is one optimiztion,
        # but it is not optimum
        if s2 % s1 != 0:
            dumb_steps = d[s1][0].steps + d[s2][0].steps + 1
        else:
            dumb_steps = d[s2][0].steps + 1
        result.append(Way(s2, s1, dumb_steps))
    d[number] = sorted(result, key=lambda e: e.steps)
    print d[number][0]
    return d[number][0].steps

f = open("result-python.txt", "w")
result = 0
for i in range(1, upperLimit):
    number = i + 1
    multiplications = dijest(number)
    sorted_path = sorted(set(path(number)), reverse=True)
    f.write("%s\n" % " ".join(map(str, sorted_path)))
    print number, multiplications, sorted_path
    result += multiplications
print "Max steps:", max(map(lambda e: e[0].steps, d.itervalues()))
print result

"""
print "\n"*25
print "==="

upperLimit = 15

#Node = namedtuple("Node", ["next", "prev"])

tree = {1 : None} #{None: (1, None)}
current = [1]
#level = []
#next_bunch = []
found = dict((i+1, None) for i in range(upperLimit))

iteration_number = 0
iteration_maximum = 5
while True:
    print iteration_number
    for number in current:
        if found[number] is None:
            found[number] = iteration_number
    print found
    iteration_number += 1
    if iteration_number == iteration_maximum:
        break


"""