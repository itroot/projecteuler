# -*- coding: utf-8 -*-

class Triangle:
    def __init__(self, raw):
        lines=raw.rstrip("\n").split("\n")
        stringFields=map(lambda l: l.split(" "), lines)
        intFields=map(lambda l: map(lambda f: int(f), l), stringFields)
        self.__data=intFields
    def size(self):
        return len(self.__data)
    def sumOfRoute(self, route):
        if (len(self.__data)<=len(route)):
            raise Exception("Invalid route")
        routeSum=self.__data[0][0]
        column=0
        row=0
        for shift in route:
            if (1==shift):
                column+=1
            row+=1
            number=self.__data[row][column]
            routeSum+=number
        return routeSum

def solve_triangle(input):
    triangle=Triangle(input)
    size=triangle.size()
    table=list(list({"maxSum": 0, "route": []} for i in range(0, size)) for i in range(0, size))
    table[0][0]["maxSum"]=triangle.sumOfRoute([])
    for depth in range(1, size):
        for width in range(0, depth):
            prevMaxRoute=table[depth-1][width]["route"]
            routeLeft=prevMaxRoute+[0]
            routeRight=prevMaxRoute+[1]
            sumLeft=triangle.sumOfRoute(routeLeft)
            sumRight=triangle.sumOfRoute(routeRight)
            if (sumLeft>table[depth][width]["maxSum"]):
                table[depth][width]["route"]=routeLeft
                table[depth][width]["maxSum"]=sumLeft
            if (sumRight>table[depth][width+1]["maxSum"]):
                table[depth][width+1]["route"]=routeRight
                table[depth][width+1]["maxSum"]=sumRight
    return max(map(lambda s: s["maxSum"], table[-1]))
