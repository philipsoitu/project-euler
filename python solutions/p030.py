sum = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        num = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        pows = a**5 + b**5 + c**5 + d**5 + e**5 + f**5
                        if num == pows:
                            print(pows)
                            sum += pows
                            
                            
print(sum-1)