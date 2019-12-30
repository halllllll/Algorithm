n, a, b = map(int, input().split())

if (b - a) % 2 == 0:
    print(b - (a + b) // 2)
else:
    # 折り返して会いにいく
    ans = 0
    if a - 1 < n - b:
        ans = a
        a, b = 1, b - a
    else:
        ans = n - b + 1
        a, b = a + (n - b) + 1, n
    print(b - (a + b) // 2 + ans)

