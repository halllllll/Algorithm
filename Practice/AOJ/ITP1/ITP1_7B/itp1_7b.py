while True:
    s = 0
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    for a in range(1, n+1):
        for b in range(a+1, min(n+1, x-a)):
            for c in range(b+1, min(n+1, x-b)):
                s += 1 if a+b+c == x else 0
    print(s)
