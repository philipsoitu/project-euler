def divisors(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    return divs


ans = 0

for i in range(1, 10000):
    a = sum(divisors(i))
    if i == sum(divisors(a)) and a != i:
        ans += i


print(ans)
