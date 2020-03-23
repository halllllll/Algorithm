# 雑に考えたら前半と後半も回文になってるってことなので判定して終了
s = input()
if s != "".join(reversed(list(s))):
    print("No")
    exit()
pre = s[:len(s) // 2]
epi = s[len(s) // 2 + 1:]

if pre == "".join(reversed(pre)) and epi == "".join(reversed(epi)):
    print("Yes")
else:
    print("No")
