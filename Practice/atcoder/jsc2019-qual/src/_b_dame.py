# まずふつうにAに含まれる転倒数をかぞえる これがK回ある
# 次にA内でAi<Ajとなる数をかぞえる これがK-1回ある
n, k = map(int, input().split())
a = list(map(int, input().split()))
x, y = 0, 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            x += 1
for i in range(n - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if a[j] < a[i]:
            print("yes i, j={}, {}".format(i, j))
            y += 1
    print()
print(x, y)
MOD = 10 ** 9 + 7

print((x * k) % MOD + (y * (k - 1)) % MOD)

