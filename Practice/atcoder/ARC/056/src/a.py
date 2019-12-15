# aだけ, bだけ、b優先、で分ける
import math

a, b, k, l = map(int, input().split())
ans_a = a * k
ans_b = math.ceil(k / l) * b
ans_c = ((k // l) * b) + ((k % l) * a)
print(min(ans_a, ans_b, ans_c))

