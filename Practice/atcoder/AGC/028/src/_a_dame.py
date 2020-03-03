# gcdより長いのは存在しなさそう（勘）なので存在するとしたらgcd
# 実際に試していく

# これだけだとTLEなるのでどっかを効率化する余地がある

n, m = map(int, input().split())
s, t = input(), input()


def lcm(a, b):
    if a > b:
        return lcm(b, a)
    while 0 != a:
        a, b = b % a, a
    return b


def gcd(a, b):
    return (a * b) // lcm(a, b)


u = gcd(n, m)
v = [None for _ in range(u)]
x1 = 0
while x1 < n:
    p = x1 * (u // n) + 1
    v[p - 1] = s[x1]
    x1 += 1
x2 = 0
while x2 < m:
    p = x2 * (u // m) + 1
    if v[p - 1] == None:
        if x2 > 0:
            v[p - 1] = t[x2]
        else:
            if s[0] == t[0]:
                continue
            else:
                print(-1)
                exit()
    else:
        if v[p - 1] != t[x2]:
            print(-1)
            exit()
    x2 += 1
print(u)
