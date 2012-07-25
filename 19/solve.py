#!/usr/bin/env python
# -*- coding: utf-8 -*-

# if 1 Jan 1900 was monday, then 1 Jan 1901 was Tuesday

class DummyDate:
    def __init__(self):
        self.__daysOfWeeks=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.__monthOfYear=[
            ("January", 31, 31),
            ("February", 28, 29),
            ("March", 31, 31),
            ("April", 30, 30),
            ("May", 31, 31),
            ("June", 30, 30),
            ("July", 31, 31),
            ("August", 31, 31),
            ("September", 30, 30),
            ("October", 31, 31),
            ("November", 30, 30),
            ("December", 31, 31)
        ]
        self.__dayNumber=0
        self.__dayOfWeek=1
        self.__dummyDate=[1, 0, 1901]
    def __isLeapYear(self, year):
        if (0==year%4):
            if (0==year%400):
                return False
            else:
                return True
        else:
            return False
    def __monthLength(self, month, year):
        monthData=self.__monthOfYear[month]
        (name, length, leapLength)=monthData
        if (self.__isLeapYear(year)):
            return leapLength
        else:
            return length
    def year(self):
        return self.__dummyDate[2]
    def dayOfWeek(self):
        return self.__dayOfWeek
    def dayOfMonth(self):
        return self.__dummyDate[0]
    def increment(self):
        self.__dayNumber+=1
        self.__dayOfWeek+=1
        self.__dayOfWeek=self.__dayOfWeek%7
        self.__dummyDate[0]=self.__dummyDate[0]+1
        if (self.__dummyDate[0]>self.__monthLength(self.__dummyDate[1], self.__dummyDate[2])):
            self.__dummyDate[1]=self.__dummyDate[1]+1
            self.__dummyDate[0]=1
        if (12==self.__dummyDate[1]):
            self.__dummyDate[1]=0
            self.__dummyDate[2]=self.__dummyDate[2]+1
    def __str__(self):
        result=str(self.__dummyDate[0])+" "
        result+=self.__monthOfYear[self.__dummyDate[1]][0]+" "
        result+=str(self.__dummyDate[2])+" "
        result+=", "+self.__daysOfWeeks[self.__dayOfWeek]
        return result
            
        
dummyDate=DummyDate()
result=0
while 2001!=dummyDate.year():
    if (6==dummyDate.dayOfWeek() and 1==dummyDate.dayOfMonth()):
        result+=1
        #print str(dummyDate)
    dummyDate.increment()
print result
