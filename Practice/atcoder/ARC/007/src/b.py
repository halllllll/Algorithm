# N100だし適当に毎回さがしてswapしてもええか
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
cur = 0
for _ in range(m):
    x = int(input())
    for j in range(n):
        if arr[j] == x:
            arr[j] = cur
            cur = x
            break
for a in arr:
    print(a)
