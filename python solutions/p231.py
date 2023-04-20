import math

def binomialCoefficient(n, k):
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n-k)
    return (a/(b*c))

# a = binomialCoefficient(20_000_000, 15_000_000)
# print("done")

a = math.factorial(900)
print(a)