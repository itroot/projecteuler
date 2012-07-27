#!/usr/bin/env python
# -*- coding: utf-8 -*-

result=0
for line in open("input.txt").readlines():
    result+=int(line)
print str(result)[0:10]
