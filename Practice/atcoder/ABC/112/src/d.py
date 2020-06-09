# これはエスパーですがMが素数ならNが何であってもできなさそう？未証明
# で 合成数のみっぽいので定石的に素因数分解すると
# 各項に因数をどれだけ割り振れるかみたいになる？
# -> サンプル1をみるとならなそう
# 最大公約数をgcdとすると、a*gcd*(N-1)+b*gcd = M となるのが都合よさそう こうなると右辺もgcdで割れるのでやはり約数のどれかになりそう
n, m = map(int, input().split())


def make_divisors(n):
    lower_divisors = []
    upper_divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)

    upper_divisors.reverse()
    return lower_divisors + upper_divisors


if m % n == 0:
    print(m // n)
    exit()
else:
    x = m // n
    divisors = make_divisors(m)[::-1]
    for d in divisors:
        if d <= x:
            print(d)
            exit()