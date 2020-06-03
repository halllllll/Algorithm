n, k, s = map(int, input().split())
if k == n:
    print(" ".join([str(s) for _ in range(n)]))
    exit()

arr = []
for i in range(1, n + 1):
    if i <= k:
        arr.append(s)
    else:
        arr.append(8 ** 9 + 14499)  # テキトー
print(" ".join(list(map(str, arr))))
