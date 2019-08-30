n = int(input())
ans = 0
for _ in range(n):
    x, y = input().split()
    x = float(x)
    if y == "JPY":
        ans += x
    else:
        ans += x * 380000.0
print(ans)
