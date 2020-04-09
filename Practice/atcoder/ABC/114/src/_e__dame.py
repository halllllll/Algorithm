# 効率よくゼロになる数を最大化するのがよさそう
# そんで残ったやつを大きい順にBの小さい方に充てる
# サンプル1は(1, 4)をゼロにするのと(1, 2)をゼロにして残った2を4から引くのとおなじになるので
# ふつうに昇順ソートした小さい方から充てていく
# 意気揚々と提出したらWAでワロタ このWAの多さはたぶんアプローチそのものを疑ったほうがいいレベルのやつ

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
start_idx = 0
for i in range(n):
    if k - a[i] >= 0:
        k -= a[i]
        a[i] = 0
    else:
        a[i] -= k
        start_idx = i
        break
ans = 10**10
for i in range(start_idx, n):
    ans = min(ans, a[i] * b[i])
print(ans)