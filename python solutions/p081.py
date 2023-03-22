f = open('files/p081_matrix.txt', 'r')


a = f.read()

a = a.splitlines()


matrix = []
for i in a:
    matrix.append(i.split(","))


# matrix = [[131, 673, 234, 103,  18],
#           [201,  96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524,  37, 331]]


for x in range(len(matrix))[::-1]:
    for y in range(len(matrix[x]))[::-1]:

        if (y != len(matrix)-1) and (x != len(matrix)-1):
            matrix[x][y] = int(matrix[x][y]) + min(int(matrix[x+1][y]), int(matrix[x][y+1]))
        # edge cases
        elif (y == len(matrix)-1) and (x != len(matrix)-1):
            matrix[x][y] = int(matrix[x][y]) + int(matrix[x+1][y])
        elif (y != len(matrix)-1) and (x == len(matrix)-1):
            matrix[x][y] = int(matrix[x][y]) + int(matrix[x][y+1])

print(matrix[0][0])