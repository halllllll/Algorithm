# 問題文読み違えてた
# 同じのが隣り合ったらダメ
# 数が同じ -> 交互に並べる
# 差が1 -> 大きいほうが外側両端をとる
# 差がそれ以上 -> はいどうしたって無理
n, m = map(int, input().split())
if n == m:
    ans = 2  # 同じ数なので入れ替えたときのやつ
    for i in range(2, n+1):
        ans *= i
        ans %= 10**9+7
        ans *= i
        ans %= 10**9+7
    print(ans)
elif abs(n - m) == 1:
    ans = 1
    for i in range(2, n+1):
        ans *= i
        ans %= 10**9+7
    for i in range(2, m+1):
        ans *= i
        ans %= 10**9+7
    print(ans)
else:
    print(0)
