# 辞書順なので後ろから当てはまるように探す
# N<=50なので全探索で構わない
s, t = input(), input()
for si in range(len(s) - len(t), -1, -1):
    flag = True
    for ti in range(len(t)):
        if s[si + ti] != t[ti] and s[si + ti] != "?":
            flag = False
            break
    if flag:
        ans = ""
        for i in range(si):
            if s[i] == "?":
                ans += "a"
            else:
                ans += s[i]
        ans += t
        for i in range(si + len(t), len(s)):
            if s[i] == "?":
                ans += "a"
            else:
                ans += s[i]
        print(ans)
        exit()
print("UNRESTORABLE")

