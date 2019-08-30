n, k = map(int, input().split())
s = input()
ans = ""
for i, c in enumerate(s):
    if i == k - 1:
        ans += c.lower()
    else:
        ans += c
print(ans)
