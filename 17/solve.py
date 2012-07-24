#!/usr/bin/env python
# -*- coding: utf-8 -*-

# one thousand
# x hundred[s] XX
# forty-two

testData={
    342: "three hundred and forty-two"
,   115: "one hundred and fifteen"
,   100: "one hundred"
,   1000: "one thousand"
}

class EnglishNumber:
    def __init__(self):
        self.__ones=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.__tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen" ,"nineteen"]
        self.__twenties = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.__thousands = ["", "thousand"]
    def __printTens(self, digits):
        length=len(digits)
        if (1==length):
            return self.__ones[digits[0]]
        elif (2==length):
            if (1==digits[0]):
                return self.__tens[digits[1]]
            else:
                optionalHyphen="-"
                twenties=self.__twenties[digits[0]]
                ones=self.__ones[digits[1]]
                if (0==len(twenties) or 0==len(ones)):
                    optionalHyphen=""
                return twenties+optionalHyphen+ones
        else:
            raise Exception("Invalid digits len: %d"%length)
    def __printHundreds(self, digit):
        return self.__ones[digit]+" hundred"
    def toString(self, number):
        if (number>1000):
            raise Exception("Can't generate numbers that no in range [1, 1000]")
        digits=map(lambda e: int(e), list(str(number)))
        length=len(digits)
        if (4==length):
            return self.__ones[1]+" "+self.__thousands[1]
        elif (3==length):
            optionalAnd=" and "
            tens=self.__printTens(digits[-2:])
            if 0==len(tens):
                optionalAnd=""
            return self.__printHundreds(digits[0])+optionalAnd+self.__printTens(digits[-2:])
        else:
            return self.__printTens(digits[-2:])

englishNumber=EnglishNumber()
for test in testData:
    englishbyHuman=testData[test]
    englishByMachine=englishNumber.toString(test)
    if englishbyHuman!=englishByMachine:
        raise Exception("Test failed: %s != %s" % (englishbyHuman, englishByMachine))

allNumbers=""
for i in range(1, 1001):
     allNumbers+=englishNumber.toString(i)
trash=allNumbers
trash="".join(trash.split("\n"))
trash="".join(trash.split(" "))
trash="".join(trash.split("-"))
print len(trash)

