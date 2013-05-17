#!/usr/bin/env python
# -*- coding: utf-8 -*-

result=1

for i in range(0, 7830457):
    result=result*2
    result=result%10**10

result=result*28433
result=result+1
result=result%10**10
print result
