#!/usr/bin/env python
# -*- coding: utf-8 -*-

# every right upper corner will contain n^2 in a such n*n spiral, 
# other coorners n^2-k*(n-1), k=1,2,3
# we can just produce simple polynomic formula

result=0
result+=1
for n in range (3, 1002, 2):
    result+=4*n**2-(1+2+3)*(n-1)
print result
