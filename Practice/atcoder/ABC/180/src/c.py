n = int(input())


def enum_div(n):
    # n自身oは含まない
    lower_divisors = []
    upper_divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)

    upper_divisors.reverse()
    return lower_divisors + upper_divisors


ans = sorted(enum_div(n))
for a in ans:
    print(a)