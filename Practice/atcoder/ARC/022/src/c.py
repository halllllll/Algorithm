# 順番に保存してみていこう 終了
n = int(input())
table = {}
ans = 0
for _ in range(n):
    x = int(input())
    if x not in table:
        table[x] = True
    else:
        ans += 1
print(ans)
