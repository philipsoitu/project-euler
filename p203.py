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
    return (primes)


def binomialCoefficient(n, k):
    def fact(n):
        if n <= 1:
            return 1
        else:
            return n*fact(n-1)
    a = fact(n)
    b = fact(k)
    c = fact(n-k)
    return (a/(b*c))



nums = set([0])

for n in range(51):
    for k in range(n+1):
        nums.add(binomialCoefficient(n, k))

primesSquared = [i**2 for i in primesUntil(int(math.sqrt(math.sqrt(max(nums)))))]

remove = 0

for n in nums:
    for ps in primesSquared:
        if n%ps==0:
            remove += n
            break

print(sum(nums))
print(remove)
print(sum(nums) - remove)