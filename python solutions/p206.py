from eulerlibrary import sqrt

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            for h in range(10):
                                for i in range(10):

                                    # 1 a 2 b 3 c 4 d 5 e 6 f 7 g 8 h 9 i 0
                                    num = int("1" + str(a) + "2" + str(b) + "3" + str(c) + "4" + str(d) + "5" + str(
                                        e) + "6" + str(f) + "7" + str(g) + "8" + str(h) + "9" + str(i) + "0")
                                    
                                    squirt = sqrt(num)

                                    if squirt*squirt == num:
                                        print(squirt)
                                                    