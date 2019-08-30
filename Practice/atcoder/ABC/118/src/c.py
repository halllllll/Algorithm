# gcdの匂いがする
# 解説読んだけどぜんぜん証明できん

n = int(input())
arr = list(map(int, input().split()))


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    while a != 0:
        a, b = b % a, a
    return b


ans = arr[0]
for i in range(1, n):
    ans = gcd(ans, arr[i])

print(ans)
