import math
from eulerlibrary import isPrime, primesUntil


def sum(array, startIndex, endIndex):
    ans = 0
    for i in range(startIndex, endIndex):
        ans += array[i]
    return ans


n = 100

primes = primesUntil(n)

startIndex = 0
endIndex = 1

highestConsecutives = 0
ans = 0

while startIndex > endIndex:

    yo = sum(primes, startIndex, endIndex)
    if yo < n:
        endIndex += 1

    if yo > n:
        startIndex += 1
        endIndex -= 1

    if isPrime(yo) and endIndex-startIndex > highestConsecutives:
        highestConsecutives = endIndex-startIndex
        ans = yo

print(ans)
