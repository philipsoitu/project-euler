"""
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symetry. 
For example, using exactly thrity-two square tiles we can form two different square laminae:

X X X X X X X X X    X X X X X X    
X               X    X X X X X X    
X               X    X X     X X    
X               X    X X     X X   
X               X    X X X X X X   
X               X    X X X X X X    
X               X
X               X
X X X X X X X X X

With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae. 

Using up to one million tiles how many different square laminae can be formed
"""

MAX_TILES = 1000000

ans = 0

outerSize = 3

while (outerSize**2-(outerSize-2)**2)<=MAX_TILES:
    innerSize = 1 + (outerSize%2==0)

    while innerSize < outerSize:
        if ((outerSize*outerSize-innerSize*innerSize) <= MAX_TILES):
            ans+=1
        innerSize+=2
    outerSize+=1

print(ans)
