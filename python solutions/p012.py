num = 1
incrementor = 2
numNotFound = True

while numNotFound:
    num += incrementor
    incrementor += 1
    factors = 0
    for i in range(1, num+1):
        if num%i==0:
            factors+=1
    if factors>500:
        numNotFound = False
        
print(num)