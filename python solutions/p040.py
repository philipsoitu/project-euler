num = "1"
i = 1
while len(num) < 1000000:
    i += 1
    num = num + str(i)
    

ans = int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])
print(ans)