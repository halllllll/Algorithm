# 「約数の個数」でググると素因数ひとつひとつに対して+1したものをかけあわせた数らしい
# あらかじめ10^3までの素数を抽出しておき、素因数を全探索、答えを更新していく
# 10^3までの素数列挙にはエラトステネスを使う

primes = []
numbers = [False for _ in range(10 ** 3 + 1)]

for i in range(2, 10 ** 3 + 1):
    if numbers[i] == False:
        primes.append(i)
        for j in range(i, 10 ** 3 + 1, i):
            numbers[j] = True

n = int(input())
ans = 1
MOD = 10 ** 9 + 7
d = {}

for i in range(2, n + 1):
    tmp = i
    for p in primes:
        while tmp % p == 0 and tmp != 0:
            d[p] = 1 if p not in d else d[p] + 1
            tmp //= p

for _, v in d.items():
    ans *= v + 1
    ans %= MOD

print(ans)
