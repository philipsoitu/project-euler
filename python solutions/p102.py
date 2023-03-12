import math

f = open('files/p102_triangles.txt', 'r')

output = f.read()

yo = output.split()
yoo =[]
for i in yo:
    yoo.append(i.split(","))


num=0
for trig in yoo:
    x1=int(trig[0])
    y1=int(trig[1])
    x2=int(trig[2])
    y2=int(trig[3])
    x3=int(trig[4])
    y3=int(trig[5])

    a = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    b = math.sqrt((x2-x3)**2 + (y2-y3)**2)
    c = math.sqrt((x3-x1)**2 + (y3-y1)**2)

    d = math.sqrt(x1**2 + y1**2)
    e = math.sqrt(x2**2 + y2**2)
    f = math.sqrt(x3**2 + y3**2)


    # check if overlap


print(num)

