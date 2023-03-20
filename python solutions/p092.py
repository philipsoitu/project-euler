import time
def nextNum(currNum):
    a = str(currNum)
    ans = 0
    for char in a:
        ans+= int(char)**2
    return ans

n = 10_000_000

ms1 = time.time()
ans=0
for i in range(1,n):

    currNum = i
    while currNum!=1:
        currNum = nextNum(currNum)
        if currNum==89:
            ans+=1
            break

ms2 = time.time()
print(f"time: {ms2-ms1}")
print(ans)