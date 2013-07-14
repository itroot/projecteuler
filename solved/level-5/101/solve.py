#!/usr/bin/env python
# -*- coding: utf-8 -*-

# see: http://en.wikipedia.org/wiki/Polynomial_interpolation#Constructing_the_interpolation_polynomial


from numpy.polynomial.polynomial import polyval, polyadd, polydiv, polymul
from fractions import Fraction as fr

# y0
# y0(x-x1)/(x0-x1)+y1(x-x0)/(x1-x0)

def interpolate(pointList):
    size = len(pointList)
    if len(pointList) == 1:
        return (fr(pointList[0][1]),)
    result = [fr(0)]
    for index_i in range(0, size):
        x_i = fr(pointList[index_i][0])
        y_i = fr(pointList[index_i][1])
        member = [y_i]
        for index_j in range(0, size):
            if index_i == index_j:
                continue
            x_j = fr(pointList[index_j][0])
            member = polymul(member, [-x_j, fr(1)])
            multiplier = [fr(1, x_i - x_j)]
            member = polymul(member, multiplier)
        result = polyadd(result, member)
    return result

polynom = map(lambda e: {True: 1, False: -1}[e%2 == 0], range(0, 11))
result = 0
length = len(polynom)
valueList = map(lambda e: (fr(e), polyval(fr(e), polynom)), range(1, length+1))
#print valueList
for i in range(0, len(polynom)):
    pointList = valueList[:i+1]
    #print pointList
    interpolation = interpolate(pointList)
    for (x, y) in valueList:
        interpolated = polyval(x, interpolation)
        if (interpolated != y):
            result += interpolated
            break

print result
