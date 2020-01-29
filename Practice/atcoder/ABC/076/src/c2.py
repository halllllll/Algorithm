# 過去に解いてたけど解き直し
# 適当に後ろから全探索して余った?はaで埋める
s, t = input(), input()
for i in range(len(s) - len(t), -1, -1):
    tt = s[i : i + len(t)]
    flag = True
    for j in range(len(t)):
        if tt[j] == t[j] or tt[j] == "?":
            continue
        else:
            flag = False
    if flag:
        ans = list(s[:i] + t + s[i + len(t) :])
        for k in range(len(s)):
            if ans[k] == "?":
                ans[k] = "a"
        print("".join(ans))
        exit()
print("UNRESTORABLE")
