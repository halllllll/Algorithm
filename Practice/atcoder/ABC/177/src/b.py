s, t = list(input()), list(input())
ans = 10**10
if len(s) == len(t):
    tmp = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            tmp += 1
    ans = min(ans, tmp)
else:
    for i in range(len(s) - len(t)):
        tmp = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                tmp += 1
        ans = min(ans, tmp)
print(ans)