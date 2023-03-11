def divisors(n):
    divs = []
    for i in range(1,n+1):
        if n%i==0:
            divs.append(i)

    return divs




for i in range(1,10000):
    a = sum(divisors(i))
    if i==sum(divisors(a)) and a!=i:
        print(i)