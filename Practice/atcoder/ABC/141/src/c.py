# 自分以外なら引かれるので
n, k, q = map(int, input().split())
d = {}
for _ in range(q):
    x = int(input())
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

for i in range(n):
    if k > q:
        print("Yes")
        continue
    if i + 1 in d and q - d[i + 1] < k:
        print("Yes")
    else:
        print("No")
