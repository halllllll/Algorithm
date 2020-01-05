# うしろから確定していく（前のやつはうしろのやつをいじれない）のでうしろからみていく。
N = int(input())
a, b = [], []
for _ in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
a = a[::-1]
b = b[::-1]
cur = 0

for i in range(N):
    if (a[i] + cur) % b[i] == 0:
        continue
    tmp = b[i] * ((a[i] + cur) // b[i] + 1) - (a[i] + cur)
    cur += tmp

print(cur)
