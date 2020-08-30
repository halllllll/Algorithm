n = int(input())
ans = [0 for _ in range(10**5)]
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            p = x**2 + y**2 + z**2 + x * y + y * z + z * x
            if p <= 10**4:
                ans[p] += 1
for i in range(1, n + 1):
    print(ans[i])