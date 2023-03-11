
a = []


for j in range(100):
    temp = []
    for i in range(100):
        temp.append(0)
    a.append(temp)


for i in range(len(a)):
    a[0][i] = i+1
    a[i][i] = 1


for i in range(1, len(a)):
    for j in range(1, len(a[i])):
        if a[i][j] == 0:
            a[i][j] = a[i][j-1] + a[i-1][j-1]

cum = (a[49][99]//2)

S = []

for i in range(1, 101):
    S.append(i**2)

print(S)

ans = 0
for num in S:
    ans += num*cum

print(ans)

# 17068293213495822407416904223283800