
def fact(n):
    if n<=1: return 1 
    else: return n*fact(n-1)

def newtonBinomialCoefficient(n, k):
    return fact(n) / (fact(k)*fact(n-k))



print(newtonBinomialCoefficient(40,20))