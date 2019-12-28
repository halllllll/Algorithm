# a*b, b*c, c*aに並べた時のmin
# 基本的に半分にぶったぎる
ans = 10 ** 18
a, b, c = map(int, input().split())
r1 = (a * b) * (c // 2)
b1 = a * b * c - r1
r2 = (b * c) * (a // 2)
b2 = a * b * c - r2
r3 = (c * a) * (b // 2)
b3 = a * b * c - r3
print(min(abs(r1 - b1), abs(r2 - b2), abs(r3 - b3)))

