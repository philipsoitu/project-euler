# f = open('files/p082_matrix.txt', 'r')


# a = f.read()

# a = a.splitlines()


# matrix = []
# for i in a:
#     matrix.append(i.split(","))


def clone2Dlist(arr):
    copyArr = []
    for x in arr:
        tempy = []
        for y in x:
            tempy.append(y)
        copyArr.append(tempy)
    return copyArr

matrix = [[131, 673, 234, 103,  18],
          [201,  96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524,  37, 331]]


shortestPath = clone2Dlist(matrix)



for y in range(len(matrix)-1)[::-1]:
    for x in range(len(matrix[y]))[::-1]:
        print(f"x: {x} , y: {y} , value: {matrix[x][y]}")
print(matrix[0][0])