# 全探索以外の方法がわからん

n = int(input())
ans = 10e9
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a * b > n:
            break
        ans = min(ans, n - a * b + abs(a - b))
print(ans)
