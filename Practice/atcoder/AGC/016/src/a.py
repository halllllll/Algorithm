from string import ascii_lowercase

s = input()

# なんかわからんけど うーん やっぱわからん
def rec(target, ss):
    if len(set(ss)) == 1:
        return len(s) - len(ss)
    tt = ""
    cc = 0
    for i in range(len(ss) - 1):
        if ss[i] == target or ss[i + 1] == target:
            tt += target
        else:
            tt += ss[i]
    return rec(target, tt)


ans = 10**10
for c in ascii_lowercase:
    ans = min(ans, rec(c, s))
print(ans)