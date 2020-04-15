k = int(input())


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b


ans = 0
for p in range(1, k + 1):
    for q in range(1, k + 1):
        for r in range(1, k + 1):
            ans += gcd(gcd(p, q), r)
print(ans)