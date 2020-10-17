# 全探索か？
# "余る"枚数なので余らせる x*y<=nにする
n = int(input())
ans = 10**10
for y in range(1, n + 1):
    x = n // y
    ans = min(ans, abs(y - x) + n - (x * y))
print(ans)
