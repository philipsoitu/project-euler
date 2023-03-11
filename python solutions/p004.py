biggestNum = 0

for i in range(1,1000):
  x = 1000-i
  for j in range(1,1000):
    y = 1000-j
    num = x*y
    reversedNum = int(str(num)[::-1])
    if num == reversedNum:
      biggestNum = max(biggestNum, num)
      

print(biggestNum)