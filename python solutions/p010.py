import math


primes = [2]
nthPrime = 1
sum=2

i=2

while i<2000000:
    i += 1
    isPrime = True
    for j in primes:
        if i%j==0 & isPrime & j<math.sqrt(i):
            isPrime = False
    if isPrime:
        primes.append(i)
        sum += i
        print(i)

print(sum)