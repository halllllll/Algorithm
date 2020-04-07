# AGC023Aたらいう地獄みたいに難しいやつのさらに上を行く地獄

n, m = map(int, input().split())
arr = list(map(int, input().split()))
b = [0]
d = {0: 1}
for i in range(n):
    b.append(b[i] + arr[i])
    if b[i + 1] % m in d:
        d[b[i + 1] % m] += 1
    else:
        d[b[i + 1] % m] = 1
ans = 0
for _, v in d.items():
    ans += (v * (v - 1)) // 2
print(ans)