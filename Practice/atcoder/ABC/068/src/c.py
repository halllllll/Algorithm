# 1からNへの経由地点Kの気持ちでみると各クエリで判別可能
n, m = map(int, input().split())
arr = [[False, False] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        arr[b - 1][0] = True
    if b == n:
        arr[a - 1][1] = True

for x in arr:
    if x[0] and x[1]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
