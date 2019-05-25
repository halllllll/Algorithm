n, k = map(int, input().split())
ans = 0
for x in range(1, n + 1):
    tmp = x
    count = 0
    while True:
        if tmp >= k:
            break
        tmp *= 2
        count += 1
    if x < k:
        ans += (1 / n) * ((1 / 2)**count)
    else:
        ans += (1/n)
    count -= 1

print(ans)
