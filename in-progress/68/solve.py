#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MagicRing:
    def __init__(self, numberList):
        length=len(numberList)
        if (length%2!=0):
            raise Exception("NumberList mut be even")
        self.__don=length/2;
        self.__numberList=numberList
        self.__internalNodes=numberList[:self.__don]
        self.__externalNodes=numberList[self.__don:]
    def __line(self, number):
        return [
            self.__externalNodes[number],
            self.__internalNodes[number],
            self.__internalNodes[(number+1)%self.__don],
        ]
    def isMagic(self):
        sumSet=set(map(lambda e: sum(self.__line(e)), range(0, self.__don)))
        return 1==len(sumSet)
    def __repr__(self):
        result=""
        position=self.__externalNodes.index(min(self.__externalNodes))
        for i in range(0, self.__don):
            offset=(i+position)%self.__don
            result+=",".join(map(lambda e: str(e), self.__line(offset)))+"; "
        return result

magicRing=MagicRing([1, 3, 2, 5, 4, 6])
print magicRing        
