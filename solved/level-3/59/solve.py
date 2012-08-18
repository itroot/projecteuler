#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Letter_frequency

codeWordLength=3

def deXor(result, participant):
    for i in range(0, 255):
        if result==participant^i:
            return i
    raise Exception("Can't deXor %d" % participant)

content=open("cipher1.txt").read().rstrip("\r\n")
encodedAsciiText=map(lambda e: int(e), content.split(","))
#print encodedAsciiText, len(encodedAsciiText)

letter2RateList=[{} for i in range(0, codeWordLength)]
for (i, letter) in enumerate(encodedAsciiText):
    letter2RateIndex=i%codeWordLength
    letter2rate=letter2RateList[letter2RateIndex]
    if not letter in letter2rate:
        letter2rate[letter]=0
    letter2rate[letter]+=1

possibleTopLetters=[" ", " ", " "]
cypherLetterList=[]

for (i, letter2rate) in enumerate(letter2RateList):
    rates=sorted(letter2rate.iteritems(), key=lambda e: e[1], reverse=True)
    #print rates
    #print
    topLetter=possibleTopLetters[i]
    cypherLetterList.append(chr(deXor(ord(topLetter), rates[0][0])))
#print cypherLetterList

decodedAsciiText=[]
for (i, letter) in enumerate(encodedAsciiText):
    decodedAsciiText.append(letter^ord(cypherLetterList[i%codeWordLength]))

text="".join(map(lambda e: chr(e), decodedAsciiText))

#print "="*80
#print text
#print "="*80

print sum(map(lambda e: ord(e), list(text)))
