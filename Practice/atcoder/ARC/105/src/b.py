n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b


x = a[0]
for i in range(1, n):
    x = gcd(x, a[i])
print(x)
