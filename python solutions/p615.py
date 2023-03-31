# doesnt work, too slow for this case

from eulerlibrary import sqrt, isPrime

def smallest_factor(n):
    for i in range(2, sqrt(n)+1):
        if n%i==0:
            return i

    return 0

yo = {}


i=1
while True:
    i+=1
    if isPrime(i):
        yo[i] = 1
    else:
        yo[i] = 1 + yo[i//smallest_factor(i)]

    if i==100:
        break

inv_yo = {v: k for k, v in yo.items()}


print(yo)
