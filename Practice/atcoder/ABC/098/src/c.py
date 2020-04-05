# 自分より左のWと右のEを数える
# 累積和だけど自分自身は見ない

n = int(input())
s = input()
lw, re = [0] * n, [0] * n
for i in range(1, n):
    if s[i - 1] == "W":
        lw[i] = lw[i - 1] + 1
    else:
        lw[i] = lw[i - 1]
for i in range(n - 2, -1, -1):
    if s[i + 1] == "E":
        re[i] = re[i + 1] + 1
    else:
        re[i] = re[i + 1]
ans = 10**10
for i in range(n):
    ans = min(ans, lw[i] + re[i])
print(ans)