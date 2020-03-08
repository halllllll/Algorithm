n, a, b = map(int, input().split())
x = n // (a + b)
ans = x * a + min(n % (a + b), a)
print(ans)
