n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b


def isprime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def div_primes(x):
    ret = {}
    for i in range(2, int(x**0.5) + 1):
        tmp = 0
        while x % i == 0:
            tmp += 1
            x //= i
        if tmp > 0:
            ret[i] = tmp
    if x > 1:
        ret[x] = 1
    return ret


f = a[0]
for i in range(1, n):
    f = gcd(a[i], f)

if f >= 2:
    print("not coprime")
    exit()

# 10^6以下の素数
hurui = [True for _ in range(10**6 + 1)]
hurui[0] = hurui[1] = False
primes = {}
for i in range(2, len(hurui)):
    if hurui[i]:
        primes[i] = 0
        for j in range(i * 2, len(hurui), i):
            hurui[j] = False

flag = True
for av in a:
    if av in primes:
        if primes[av] == 0:
            primes[av] = 1
        else:
            flag = False
            break
    else:
        divs = div_primes(av)
        for k in divs.keys():
            if primes[k] == 0:
                primes[k] = 1
            else:
                flag = False
                break
    if flag == False:
        break

if flag:
    print("pairwise coprime")
else:
    print("setwise coprime")

# 6
# 4 7 9 11 5 13