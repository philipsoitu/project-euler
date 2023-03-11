maxTerms = 0 

for i in range(1,1000000):
    terms = 1

    n=i
    while n != 1:
    
        if n%2 == 0:
            n = n/2
        elif n%2 == 1:
            n = 3*n+1
        terms +=1
    print(f"{i} : {terms}")

    if terms>maxTerms:
        maxTerms = max(maxTerms, terms)
        ans = i


print(ans)