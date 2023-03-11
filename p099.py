# theres definetly a faster way to do this with logs, but idc

f = open("files/p099_base_exp.txt", "r")
n = f.read()

list = n.splitlines()

nums = []
for i in list:
    temp = i.split(',')
    nums.append(temp)


biggestNum = 0

for i in range(1000):
    print(i) 
    n = int(nums[i][0])**int(nums[i][1])
    if n > biggestNum:
        biggestNum = n
        index = i
        


print(index)