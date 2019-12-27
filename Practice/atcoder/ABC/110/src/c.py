# 1対1なので決めていく
s, t = input(), input()
sd, td = {}, {}
for i in range(len(s)):
    if t[i] not in td and s[i] not in sd:
        sd[s[i]] = t[i]
        td[t[i]] = s[i]
    elif t[i] in td and s[i] in sd and td[t[i]] == s[i] and sd[s[i]] == t[i]:
        continue
    else:
        print("No")
        exit()
print("Yes")
