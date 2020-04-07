# 適当にやってたら出た
# と思ったら対応できてないケースがある（それはそう）

import math
a, b, c = map(int, input().split())
if a == b == c:
    print((a + b + c)**2 * math.pi)
elif a >= b and a >= c:
    print((a + b + c)**2 * math.pi - (a - b - c)**2 * math.pi)
elif c >= a and c >= b:
    print((a + b + c)**2 * math.pi - (c - a - b)**2 * math.pi)
elif b >= a and b >= c:
    print((a + b + c)**2 * math.pi - (b - a - c)**2 * math.pi)
else:
    print(0 / 0)
