#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import factorial

upperLimit = 15

start = {
    "R" : 1,
    "B" : 1,
    }
red_disk_number = 2

for i in range(upperLimit-1):
    new_start = {}
    for (key, value) in start.iteritems():
        new_start[key+"B"] = value
        new_start[key+"R"] = value*red_disk_number
    red_disk_number += 1
    start = new_start
print factorial(upperLimit+1)/sum(map(lambda e: e[1], filter(lambda (e, _): len(filter(lambda i: i == "B", e))>upperLimit/2, start.iteritems())))