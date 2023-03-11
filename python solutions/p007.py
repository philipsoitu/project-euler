import math

primes = [2]
nthPrime = 1

i=2

while nthPrime<10001:
    i += 1
    isPrime = True
    for j in primes:
        if i%j==0 & isPrime & j<math.sqrt(i):
            isPrime = False
    if isPrime:
        primes.append(i)
        nthPrime +=1

print(primes[len(primes)-1])