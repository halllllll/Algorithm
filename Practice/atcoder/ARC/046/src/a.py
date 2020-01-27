# 9個ごとに一桁増える
n = input()
if len(n) == 1:
    print(n)
n = int(n)
a = n // 9
b = n % 9
print(str(a) * b)

