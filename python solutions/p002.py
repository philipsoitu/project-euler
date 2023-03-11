a=1
b=1
sum = 0 
ans = 0

while sum<=4000000:
    sum = a+b
    a=b
    b=sum
    if sum%2==0:
        ans = ans + sum
        
print(ans)
