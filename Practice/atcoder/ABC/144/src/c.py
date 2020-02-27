# a-bが最小となる、a*b=nを満たすa,b(a>=b)を見つける作業。
# 素因数分解してすべての組み合わせで2数を作って...と考えたけどあきらかにダルい
# ダルいので全探索。1から順に割って、割り切れた数をbとする
# 10^12とデカイが、a*b=n(a>=b)と考えた時、a*a>=nだし、せいぜいaは平方根までの探索でいい
n = int(input())
ans = 10 ** 13

for v in range(1, int(n ** 0.5) + 1):
    a = v
    if n % a != 0:
        continue
    b = n // a
    ans = min(ans, a - 1 + b - 1)

print(ans)
