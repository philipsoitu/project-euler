#def pascal(n):
#
#    if n == 2:
#        return[1,1]
#    else:
#        triangle = [1]
#        for i in range(n-2):
#            triangle.append(pascal(n-1)[i]+pascal(n-1)[i+1])
#            print(n)
#        triangle.append(1)
#    
#    return triangle
#
#
#print(pascal(4))


#better solution
def fact(n):
    if n<=1: return 1 
    else: return n*fact(n-1)

def newtonBinomialCoefficient(n, k):
    return fact(n) / (fact(k)*fact(n-k))



print(newtonBinomialCoefficient(40,20))