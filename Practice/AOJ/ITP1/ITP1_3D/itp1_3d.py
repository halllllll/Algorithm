a, b, c = map(int, input().split())
ans = 0
for x in range(a, b+1):
    if c % x == 0:
        ans += 1
print(ans)
