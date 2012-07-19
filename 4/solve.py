#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPalindromic(number):
    s=str(number)
    if (0!=len(s)%2):
        return False
    halfLen=len(s)/2
    return s[0:halfLen]==s[halfLen:][::-1]


palindromic=[]

for num1 in range(900, 999):
    for num2 in range(900, 999):
        num=num1*num2
        if isPalindromic(num):
            palindromic.append(num)

print palindromic[-1]
