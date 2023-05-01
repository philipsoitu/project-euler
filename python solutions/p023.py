# returns sum of factors excluding n
def sumFactors(n):
    fact = set()
    for i in range(1,n):
        if n%i==0:
            fact.add(i)
    return sum(fact)


abundant_numbers = set()

for i in range(28124):

    if sumFactors(i)>i:
        # abundant number
        abundant_numbers.add(i)
        
print("abundant numbers found")

sum_of_abundant = set()
for num1 in abundant_numbers:
    for num2 in abundant_numbers:
        sum_of_abundant.add(num1+num2)

print("found sum of abundant numbers")

excluding_big_nums = set()

for num in sum_of_abundant:
    if num<28124:
        excluding_big_nums.add(num)

all_nums = set()

for i in range(28124):
    all_nums.add(i)

print("created set of all numbers until 28124")

ans_set = all_nums ^ excluding_big_nums


print(sum(ans_set))