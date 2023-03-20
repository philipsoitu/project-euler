fibonacci = [1,1]
index = 1


while len(str(fibonacci[index]))<1000:
    fibonacci.append(fibonacci[index] + fibonacci[index-1])
    index+=1


print(index+1)