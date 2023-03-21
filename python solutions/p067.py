f = open('files/p067_triangle.txt')

a = f.read()
tree = []
a = a.splitlines()
for i in a:
    tree.append(i.split(" "))



for i in range(len(tree)-1)[::-1]:
    for j in range(len(tree[i])):
        tree[i][j] = int(tree[i][j]) + max(int(tree[i+1][j]), int(tree[i+1][j+1]))

print(tree[0][0])