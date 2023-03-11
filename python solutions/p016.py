ans = 0
num = 1

for i in range(1000):
  num*=2

for i in range(int(len(str(num)))):
  ans += int(str(num)[i:i+1])
print(ans)