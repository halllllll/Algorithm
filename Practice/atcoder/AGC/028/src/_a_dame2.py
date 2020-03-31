# 「最小公倍数以上でも作れる」と思ったけどそういうことはないのでは？
# 実際に試してみてどうなるか判定みたいな感じでやっていく
n, m = map(int, input().split())
s = input()
t = input()


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    while a != 0:
        a, b = b % a, a
    return b


def lcm(a, b):
    return (a * b) // gcd(a, b)


xlength = lcm(n, m)
if xlength == n or xlength == m:
    print(-1)
    exit()
ans = [0 for _ in range(n * m)]
for i in range(1, n):
    target = (xlength // n + 1) * 1
    ans[target] = s[i - 1]
for i in range(1, m):
    target = (xlength // m + 1) * 1
    if ans[target] != 0:
        print(-1)
        exit()
    ans[target] = t[i - 1]
print(ans)
