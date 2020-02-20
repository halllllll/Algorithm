# やりましょう おわり
n = int(input())
ans = 0

for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    ans = max(ans, sum([a, b, c, d]) + e * (110 / 900))
print(ans)
