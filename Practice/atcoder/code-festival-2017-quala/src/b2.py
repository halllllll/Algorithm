n, m, k = map(int, input().split())
if n == 1 or m == 1:
    print("Yes")
    exit()
# これ必要か？？？？？？？？？？
# -> 意味不明だが必要らしい...
if k % n == 0 or k % m == 0:
    print("Yes")
    exit()
for p in range(n + 1):
    for q in range(m + 1):
        if p * (m - q) + q * (n - p) == k:
            print("Yes")
            exit()
print("No")