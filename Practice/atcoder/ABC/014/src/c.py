# imos
n = int(input())

arr = [0 for _ in range(10 ** 6 + 2)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b + 1] -= 1
# 整列アンド探索フェーズ
ans = arr[0]   # n,a,b=1,0,0の場合があったので
for i in range(1, 10 ** 6 + 2):
    arr[i] += arr[i - 1]
    ans = max(ans, arr[i])
print(ans)
