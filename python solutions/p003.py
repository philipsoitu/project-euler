import math

primes = [2]
for i in range(2,10000):
  isPrime = True
  for j in primes:
    if i%j==0 & isPrime & j<math.sqrt(i):
      isPrime = False
  if isPrime:
    primes.append(i)


biggestPrime = 0
num = 600851475143

for p in primes:
  if num%p==0:
    num = num/p
    biggestPrime = max(biggestPrime, p)

print(num)
print(biggestPrime)