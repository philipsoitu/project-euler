f = open("files/p059_cipher.txt", "r")

a = (f.read().split(","))

for i in range(len(a)):
    a[i] = int(a[i])





def decrypt(key, input):
    for i in range(len(input)):
        currChar = ord(key[i%len(key)])
        input[i] = input[i] ^ currChar
    return input





print(decrypt("a", [65]))

secretkey = []
for char1 in range(256):
    for char2 in range(256):
        for char3 in range(256):
            secretkey.append(chr(char1) + chr(char2) + chr(char3))

