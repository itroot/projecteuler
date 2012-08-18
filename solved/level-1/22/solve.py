#!/usr/bin/env python
# -*- coding: utf-8 -*-

data=open("names.txt").read()
names=map(lambda name: name.strip("\""), data.split(","))
sortedNames=sorted(names)

def name2number(name):
    result=0
    for letter in name:
        result+=ord(letter)-ord("A")+1
    return result

result=0
for i in range(0, len(sortedNames)):
    result+=name2number(sortedNames[i])*(i+1)
print result
