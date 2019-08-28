# 問題文の謎の式の意味はわからんが、要はM個の状態の数だけあるわけだ
n, m = map(int, input().split())
a = (1900 * m + 100 * (n - m)) * (1 << m)
print(a)
