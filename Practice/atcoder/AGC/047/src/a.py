# どこを選んでもかまわん
n, m, k = map(int, input().split())
for i in range(n + 1):
    for j in range(m + 1):
        black = i * m - (j * i) + (n - i) * j
        if black == k:
            print("Yes")
            exit()
print("No")
