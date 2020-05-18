import math
a, b, h, m = map(float, input().split())
mm = (m % 60.0) * 6.0
hh = h * 30.0 + m * 0.5

rad = (mm - hh) * math.pi / 180.0
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2 * a * b * math.cos(rad))

print(c)
