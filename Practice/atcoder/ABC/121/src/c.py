# Aiで貪欲する
# kが何度も登場するっていう罠？

n, m = map(int, input().split())
h = dict()
for _ in range(n):
    k, v = map(int, input().split())
    if k in h:
        h[k] += v
    else:
        h[k] = v
h = sorted(h.items(), key=lambda x: x[0])


ans = 0
for k, v in h:
    while v > 0:
        if m <= 0:
            print(ans)
            exit()
        else:
            v -= 1
            ans += k
            m -= 1
print(ans)
