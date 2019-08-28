# ソートしてでかいやつから+-するだけ
import math  # for pi
n = int(input())

arr = list(reversed(sorted([float(input())
                            for _ in range(n)])))  # pythonのここがキモい

s = 0
red = True
for ai in arr:
    if red:
        s += (ai*ai*math.pi)
        red = False
    else:
        s -= (ai*ai*math.pi)
        red = True

print(s)
