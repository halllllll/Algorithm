# 最も少ない箇所がボトルネックになる（ので、5つ全部が最小値のときと結果が同じ
import math
n = int(input())
minn = min([int(input()) for _ in range(5)])
print(math.ceil(n/minn)+4)
