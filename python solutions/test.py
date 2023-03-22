import math

k = 200

points = []

# s0
s = [290797]

# s 2k+1
for i in range(0,k*2-1):
    s.append((s[i]**2) % 50515093)
    
minDist = 99999999999999999999999999

for a in range(k-1):
    print(a)
    for b in range(a+1,k):
        dX = s[b*2] - s[a*2]
        dY = s[b*2+1] - s[a*2+1]
        minDist = min(minDist, math.sqrt(dX*dX+dY*dY))
        
print(f"minDist :   {minDist}")
print(f"delta x :   {dX}")
print(f"delta y :   {dY}")