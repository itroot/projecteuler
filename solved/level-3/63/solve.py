#!/usr/bin/env python
# -*- coding: utf-8 -*-

upperLimit=99

result=0

for number in range(1, upperLimit):
    for power in range(1, upperLimit):
        if len(str(number**power))==power:
            result+=1
            #print number, "**", power

print result
