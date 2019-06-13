# Nが素数のときはNの桁数しかない
# 3桁*3桁 = 6桁 3桁*4桁=6~7桁 2桁*6桁=7~8桁なのでNの桁数がわかればA,Bの桁数が分かる
# A<=BとするとN=10だと(1,9)|(1,10)(2,8)|(2,9)(3,7)|(3,8)(4,6)|(4,7)|(5,5)
# * 最初の(1,9)の一桁では1は素数で省かれているので除く
# なのでせいぜい10^5まで調べりゃいい
n = int(input())


def f(t):
    keta = 0
    while t > 0:
        keta += 1
        t //= 10
    return keta


flag = False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        flag = True
        break

if flag is False:
    print(f(n))
    exit()

maxn = 10**9
for a in range(2, 10 ** 6):
    if n % a == 0:
        b = n / a
        maxn = min(maxn, max(f(b), f(a)))

print(maxn)
