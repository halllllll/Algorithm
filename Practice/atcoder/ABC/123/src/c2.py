# ボトルネック+4
from math import ceil
n = int(input())
neck = min([int(input()) for _ in range(5)])
m = ceil(n / neck)
print(m + 4)
