n = int(input())
ans = 0

for i in range(1, n):
    for j in range(i, n, i):
        ans += 1
print(ans)
