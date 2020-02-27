# しらんけど
# ふつうにこれやったらTLEなったのでアレする
# n = int(input())
# print(sum(range(n)))

n = int(input())
if n % 2 == 0:
    a = (1 + n) * (n // 2)
    print(a - n)
else:
    a = (1 + n) * ((n - 1) // 2) + (n // 2 + 1)
    print(a - n)

