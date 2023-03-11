import math

def primesUntil(n):
    primes = [2]
    for i in range(3, n, 2):

        isPrime = True
        squirt = math.sqrt(i)
        for j in primes:
            if i % j == 0 & isPrime & i < squirt:
                isPrime = False
        if isPrime:
            primes.append(i)
            print(i)
    return (primes)


primes = primesUntil(1001)
highestPrimeSum = 0
sum = 0


for p in primes:
    sum+=p
    if sum in primes:
        highestPrimeSum = sum
        print(highestPrimeSum)
    if sum > 1001:
        break

print(highestPrimeSum)