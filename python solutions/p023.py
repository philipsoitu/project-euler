# returns sum of factors excluding n
def sumFactors(n):
    fact = set()
    for i in range(1,n):
        if n%i==0:
            fact.add(i)
    return sum(fact)

print(sumFactors(10))



for i in range(100):

    if sumFactors(i)>i:
        # abundant number
        print(f"{i} is abundant")
    elif sumFactors(i)<i:
        # deficient number
        print(f"{i} is deficient")
    else: 
        # perfect number
        print(f"{i} is perfect")

        