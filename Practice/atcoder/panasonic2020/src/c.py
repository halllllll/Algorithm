from decimal import *
a, b, c = map(int, input().split())
if Decimal(a)**Decimal("0.5") + Decimal(b)**Decimal("0.5") < Decimal(
        c)**Decimal("0.5"):
    print("Yes")
else:
    print("No")
