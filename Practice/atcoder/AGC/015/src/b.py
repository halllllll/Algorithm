s = input()
ans = 0
for idx, v in enumerate(s):
    l, r = idx, len(s) - (idx + 1)
    if v == "U":
        ans += l * 2 + r
    else:
        ans += l + r * 2

print(ans)
