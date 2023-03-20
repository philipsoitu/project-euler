import math


# binomial coefficient
def binomial(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


# floored sqrt
def sqrt(n):

    i = 1
    while i * i <= n:
        i *= 2

    y = 0
    while i > 0:
        if (y + i)**2 <= n:
            y += i
        i //= 2
    return y


def triangleNumber(k):
    return (k*(k+1)//2)



#prime generator until n
def primesUntil(n):
    primes = [2]
    for i in range(3, n+1, 2):

        isPrime = True
        squirt = math.sqrt(i)
        for j in primes:
            if i % j == 0 & isPrime & j < squirt:
                isPrime = False
        if isPrime:
            primes.append(i)
    return (primes)


def isPrime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(n) + 1, 2):
			if n % i == 0:
				return False
		return True


# area of triangle 
def areaOfTriangle(Ax, Ay, Bx, By, Cx, Cy):
    return abs((Ax*(By - Cy) + Bx*(Cy - Ay) + Cx*(Ay - By)) / 2)

