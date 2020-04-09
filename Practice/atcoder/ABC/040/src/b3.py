# よくわからんけどとりあえずやってみるやつ
n = int(input())
ans = 10**10
for i in range(1, n + 1):
    for j in range(1, n // i + 1):
        if i * j > n:
            continue
        ans = min(ans, abs(i - j) + (n - (i * j)))
print(ans)