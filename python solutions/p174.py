"""
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symetry. 

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle. 
However, using thirty-two tiles it is possible to form two distinct laminae.

X X X X X X X X X    X X X X X X    
X               X    X X X X X X    
X               X    X X     X X    
X               X    X X     X X   
X               X    X X X X X X   
X               X    X X X X X X    
X               X
X               X
X X X X X X X X X

If t represents the number of tiles used, we shall say that t=8 is type L(1) and t=32 is type L(2).

Let N(n)be the number of t <= 1 000 000 such that t is type L(n); for example, N(15) = 832
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
