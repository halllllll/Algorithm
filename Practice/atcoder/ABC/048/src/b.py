a, b, x = map(int, input().split())
print((b//x) - (a//x) + (1 if a % x == 0 else 0))