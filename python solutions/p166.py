"""
A 4x4 grid is filled with digits d , 0 <= d <= 9,
It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d , 0 <= d <= 9 so that each row, each column, and both diagonals have the same sum?
"""

"""
a b c d
e f g h
i j k l
m n o p

= a + b + c + d
= e + f + g + h
= i + j + k + l
= m + n + o + p
= a + e + i + m
= b + f + j + n
= c + g + k + o
= d + h + l + p
= a + f + k + p
= d + g + j + m


"""


def possibleSummations(n):
    ans = []
    for a in range(10):
        for b in range(10):
            if (a+b) > n:
                break
            for c in range(10):
                if (a+b+c) > n:
                    break
                for d in range(10):
                    if (a+b+c) > n:
                        break
                    if (a+b+c+d) == n:
                        ans.append([a, b, c, d])
    return ans


for sum in range(37):
    ans = 0
    arr = possibleSummations(sum)
    for a in arr:
        for b in arr:
            if (a[0]+b[0]>=sum) or (a[1]+b[1]>=sum) or (a[2]+b[2]>=sum) or (a[3]+b[3]>=sum) or (a[0]+b[1]>=sum) or (a[3]+b[2]>=sum):
                break
            for c in arr:
                if (a[0]+b[0]+c[0]>=sum) or (a[1]+b[1]+c[1]>=sum) or (a[2]+b[2]+c[2]>=sum) or (a[3]+b[3]+c[3]>=sum) or (a[0]+b[1]+c[2]>=sum) or (a[3]+b[2]+c[1]>=sum):
                    break
                for d in arr:
                    if (a[0] + b[0] + c[0] + d[0] == sum) and (a[1] + b[1] + c[1] + d[1] == sum) and (a[2] + b[2] + c[2] + d[2] == sum) and (a[3] + b[3] + c[3] + d[3] == sum) and (a[0] + b[1] + c[2] + d[3] == sum) and (a[3] + b[2] + c[1] + d[0] == sum):
                        ans += 1
    print(sum, ans)

print(ans)


possibilitiesDependingOnSum = {
    0: 1,
    1: 8,
    2: 48,
    3: 200,
    4: 675,
    5: 1904,
    6: 4736,
    7: 10608,
    8: 21925,
    9: 42328,
    10: 76976,

}
