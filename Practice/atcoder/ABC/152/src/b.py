a, b = input().split()
axb, bxa = a * int(b), b * int(a)
print(min(axb, bxa))
