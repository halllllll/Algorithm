# DFSかと思いきや時系列に得られるので単にシミュするだけだった
n = int(input())
t1, t2 = [], []
words = []
for i in range(n):
    w = input()
    if i % 2 == 0:
        if len(t1) == 0:
            # 初手
            t1.append(w)
            words.append(w)
        else:
            p = t2[-1]
            if p[-1] == w[0] and w not in words:
                t1.append(w)
                words.append(w)
            else:
                print("LOSE")
                exit()
    else:
        p = t1[-1]
        if p[-1] == w[0] and w not in words:
            t2.append(w)
            words.append(w)
        else:
            print("WIN")
            exit()
print("DRAW")
