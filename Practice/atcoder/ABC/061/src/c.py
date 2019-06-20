# 配列じゃなくて辞書なり連想配列なりハッシュなりを使いましょう おしまい
n, k = map(int, input().split())
h = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a in h:
        h[a] += b
    else:
        h[a] = b

arr = [x for x in h.items()]
arr = list(sorted(arr, key=lambda x: x[0]))
count = 0

for a in arr:
    if count + a[1] >= k:
        print(a[0])
        exit()
    else:
        count += a[1]
