k, x = map(int, input().split())
ans = []
for i in range(x - k + 1, x - k + 1 + 2 * k - 1):
    ans.append(i)
print(" ".join(list(map(str, ans))))

