import math
from eulerlibrary import *

f = open('files/p102_triangles.txt', 'r')

output = f.read()

yo = output.split()
yoo = []
for i in yo:
    yoo.append(i.split(","))


num = 0
for trig in yoo:
    x1 = int(trig[0])
    y1 = int(trig[1])
    x2 = int(trig[2])
    y2 = int(trig[3])
    x3 = int(trig[4])
    y3 = int(trig[5])

    # check if overlap
    # print(x1,y1,x2,y2,x3,y3)

    area = areaOfTriangle(x1, y1, x2, y2, x3, y3)
    y = areaOfTriangle(0, 0, x2, y2, x3, y3) + areaOfTriangle(x1,
                                                              y1, 0, 0, x3, y3) + areaOfTriangle(x1, y1, x2, y2, 0, 0)
    if area == y:
        num += 1

print(num)
