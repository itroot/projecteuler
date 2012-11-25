#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

class MagicRing:
    def __init__(self, numberList):
        length=len(numberList)
        if (length%2!=0):
            raise Exception("NumberList mut be even")
        self.__don=length/2;
        #self.__numberList=numberList
        self.__internalNodes=numberList[:self.__don]
        self.__externalNodes=numberList[self.__don:]
    def __line(self, number):
        return (
            self.__externalNodes[number],
            self.__internalNodes[number],
            self.__internalNodes[(number+1)%self.__don],
        )
    def line(self, number):
        return self.__line(number)
    def isMagic(self):
        firstSum=sum(self.__line(0))
        for i in range(1, self.__don):
            if (sum(self.__line(i))!=firstSum):
                return False
        return True
        #sumSet=set(map(lambda e: sum(self.__line(e)), range(0, self.__don)))
        #return 1==len(sumSet)
    def __repr__(self):
        result=""
        position=self.__externalNodes.index(min(self.__externalNodes))
        for i in range(0, self.__don):
            offset=(i+position)%self.__don
            result+="".join(map(lambda e: str(e), self.__line(offset)))
        return result

upperLimit=10
allNotations=set()
for (i, numberList) in enumerate(itertools.permutations(range(1, upperLimit+1))):
    #if i%100000==0:
    #    print i 
    magicRing=MagicRing(numberList)
    if magicRing.isMagic():
        allNotations.add(str(magicRing))
#print allNotations
print max(map(lambda e: int(e), filter(lambda e: len(e)==16, list(allNotations))))
