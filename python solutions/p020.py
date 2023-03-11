def fact(n):
    if n>1:
        return n * fact(n-1)
    else:
        return 1

ans = str(fact(100))

sum = 0
for i in range(len(ans)):
    sum += int(ans[i])


print(sum)