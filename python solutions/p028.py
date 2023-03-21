ans = 1

n = 1001
step = n-1
currNum = n*n

while step>0:
    for i in range(4):
        ans+= currNum
        currNum -= step
    step -=2

print(ans)