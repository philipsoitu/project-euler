f = open('files/p022_names.txt', 'r')

alphaToNum = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

output = f.read()
yo = output.split(",")
names = []
for i in yo:
    names.append(i[1:-1])
names.sort()


ans = 0
for index in range(len(names)):
    currName = names[index]
    mult = 0
    for char in currName:
        mult+= alphaToNum[char]
    ans += mult*(index+1)

print(ans)