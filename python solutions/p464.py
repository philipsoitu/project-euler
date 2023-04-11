

"""
the mobius function, denoted u(n), is defined as: 
u(n) = (-1)^(w(n)) if n is squarefree (where w(n) is the number of distinct prime factors of n)
u(n) = 0 if n is not squarefree

Let P(a,b) be the number of integers n in the interval [a,b] such that u(n) = 1
Let N(a,b) be the number of integers n in the interval [a,b] such that u(n) = -1
For example P(2,10) = 2 and N(2,10) = 4

Let C(n) be the number of integer pairs (a,b) such that:

1 <= a <= b <= n
99 * N(a,b) <= 100 * P(a,b) and 
99 * P(a,b) <= 100 * N(a,b)

For example, C(10) = 13, C(500) = 16676 and C(10 000) = 20155319

Find C(20 000 000)

_____________________________________________________________________________________________

A squarefree number is an integer which is not divisible by any square number other than 1
for example: 
10 is squarfree since 2 * 5, but 
18 is not because 2 * 3 * 3, and 3^2 = 9

"""


import time


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


def smallest_factor(n):
    for i in range(2, sqrt(n)+1):
        if n % i == 0:
            return i

    return 0


def mobius(n):

    yo = {1: [True, [], ]}

    for i in range(2, n+1):
        a = smallest_factor(i)
        if a != 0:  # not prime
            if not (yo[i//a][0]) or a == yo[i//a][1][0]:
                yo[i] = [False, yo[i//a][1]]
            else:
                yo[i] = [True, [a] + yo[i//a][1]]
        else:  # prime
            yo[i] = [True, [i]]

    morb = {}
    for i in range(1, n+1):
        morb[i] = (-1)**(len(yo[i][1])) * int(yo[i][0])

    return morb


t1 = time.time()
N = 500

morb = mobius(N)


c=0
for a in range(1, N+1):
    for b in range(a, N+1):
        p = 0
        n = 0
        for i in range(a, b+1):
            if morb[i] == 1:
                p += 1
            if morb[i] == -1:
                n += 1

        if (99*n <= 100*p) and (99*p <= 100*n):
            c+=1

print(c)


t2 = time.time()
print(t2-t1)
