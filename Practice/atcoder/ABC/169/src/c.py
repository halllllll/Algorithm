from decimal import *
import math
a, b = map(str, input().split())
a, b = Decimal(a), Decimal(b)
print(math.floor(a * b))
