import math


def primesUntil(n):
    primes = [2]
    for i in range(3, n, 2):

        isPrime = True
        squirt = math.sqrt(i)
        for j in primes:
            if i % j == 0:
                isPrime = False

            if not (isPrime) or j > squirt:
                break
        if isPrime:
            primes.append(i)
            print(i)
    return (primes)


n = 50

primes = primesUntil(n)
highestJ = 0
ans = 0
sum=0

for i in range(len(primes)):
    sum += primes[i]
    for j in range(i+1,len(primes)):
        sum+= primes[j]
        if not(sum in primes) or sum>n:
            sum-=primes[j]
            break
    
    if (j-i)> highestJ:
        ans = sum
        highestJ = j

print(ans)
