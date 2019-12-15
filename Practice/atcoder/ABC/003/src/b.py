# recommendからきました
# 同じインデックスを調べるだけ
s, t = input(), input()
atcoder = list("atcoder")
flag = True
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    if s[i] == "@":
        if t[i] in atcoder:
            continue
        else:
            flag = False
    elif t[i] == "@":
        if s[i] in atcoder:
            continue
        else:
            flag = False
    else:
        flag = False

print("You can win" if flag else "You will lose")
