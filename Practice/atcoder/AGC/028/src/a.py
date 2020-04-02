# たぶん最小の値は最小公倍数になりそう
# 内包表記 -> TLE
# [0]*l -> RE
# しかたねぇから辞書でやることにする -> AC

n, m = map(int, input().split())
s, t = input(), input()


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    while a > 0:
        a, b = b % a, a
    return b


def lcm(a, b):
    return (a * b) // gcd(a, b)


l = lcm(n, m)
arr = {}

for i in range(n):
    x = i * (l // n)
    arr[x] = s[i]

for i in range(m):
    x = i * (l // m)
    if x in arr and arr[x] != t[i]:
        print(-1)
        exit()
print(l)