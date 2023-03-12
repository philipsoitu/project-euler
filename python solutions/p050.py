import math


def isPrime(n, primes):
    lim = math.sqrt(n)
    for p in primes:
        if n % p == 0:
            return False

        if lim < p:
            break
    return True


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


n = 1000000

primes = primesUntil(n)

highestCons = 0
highestPrime = 0


for i in range(len(primes)):
    sum = primes[i]

    if sum > n:
        break

    for j in range(i+1, len(primes)-i):
        sum += primes[j]
        
        if sum>n:
            break
        
        # if isPrime(sum, primes):
        #     if (j-i)>highestCons
