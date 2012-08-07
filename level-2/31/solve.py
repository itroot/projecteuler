#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bisect import *

coins=[1, 2, 5, 10, 20, 50, 100, 200]
def generateAllCoins(amount, coins):
    result=[]
    if amount==0:
        result.append([])
    elif amount==coins[0]:
        result.append([coins[0]])
    else:
        maxCoin=bisect_left(coins, amount+1)-1
        #maxCoinValue=coins[maxCoin]
        for coin in range(0, maxCoin+1):
            coinValue=coins[coin]
            #print coinValue
            lists=generateAllCoins(amount-coinValue, coins[0:coin+1])
            #print "Lists:", lists
            result+=map(lambda e: e.append(coinValue) or e, lists)
    #print "Result:", amount, coins, result
    return result

result=generateAllCoins(200, coins)
print len(result)
