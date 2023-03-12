import math

def isPrime(num):
    
    for i in range(2,math.sqrt(num) +1 , 2):
        if (num%i==0):
            return False
        
    return True


def nextPrime(pArray):
  n = pArray[-1]
  notPrime = True
  while notPrime:
    n += 2
    notPrime = False
    for i in range(len(pArray)):
      if (n%pArray[i] == 0):
        notPrime = True
  pArray.append(n)
  return pArray


p = [2,3,5,7]
numOfPallindromesFound = 0
sum = 0

while numOfPallindromesFound<50:
    p = nextPrime(p)
    if isPrime(math.sqrt(p[-1])):
        numOfPallindromesFound+=1
        sum+=p[-1]


# wip