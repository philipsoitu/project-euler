def numberWordifier(a, b, c):
    onesPlace = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        
    }
    tensPlace = {
        0 : "",
        1 : "weird case ",
        2 : "twenty ",
        3 : "thirty ",
        4 : "forty ",
        5 : "fifty ",
        6 : "sixty ",
        7 : "seventy ",
        8 : "eighty ",
        9 : "ninety ",
    }

    hundredsPlace = {
        0 : "",
        1 : "one hundred ",
        2 : "two hundred ",
        3 : "three hundred ",
        4 : "four hundred ",
        5 : "five hundred ",
        6 : "six hundred ",
        7 : "seven hundred ",
        8 : "eight hundred ",
        9 : "nine hundred ",
    }

    weirdCase = {
        0 : "ten",
        1 : "eleven",
        2 : "twelve",
        3 : "thirteen",
        4 : "fourteen",
        5 : "fifteen",
        6 : "sixteen",
        7 : "seventeen",
        8 : "eighteen",
        9 : "nineteen",
    }


    if a!=0 and b+c!=0:
        if b ==1:
            num = hundredsPlace[(a)] + "and "+ weirdCase[c]
        else:
            num = hundredsPlace[(a)] + "and " + tensPlace[(b)] + onesPlace[(c)]
    else:
        if b ==1:
            num = hundredsPlace[(a)] + weirdCase[c]
        else:
            num = hundredsPlace[(a)] + tensPlace[(b)] + onesPlace[(c)]

    return num



ans =0
for a in range(10):
    for b in range(10):
        for c in range(10):
            word = numberWordifier(a,b,c)
            for char in word:
                if char != " ":
                    ans+=1
            print(word)

print(ans+11)