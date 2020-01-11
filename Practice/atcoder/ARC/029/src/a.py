# Nめっちゃ小さいな アドホックでいいんじゃね
n = int(input())
if n == 1:
    print(input())
    exit()
if n == 2:
    print(max(int(input()), int(input())))
    exit()
if n == 3:
    a, b, c = sorted([int(input()) for _ in range(n)])
    print(max(a + b, c))
    exit()
if n == 4:
    a, b, c, d = sorted([int(input()) for _ in range(n)])
    # (a+b+c, d), (a+b, c+d), (a+c, b+d)
    print(
        min(max(a + b + c, d), max(a + b, c + d), max(a + d, c + b), max(a + c, b + d))
    )
