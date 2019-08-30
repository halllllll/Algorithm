# 包除原理, cとdの最小公倍数, b-aではなく b-(a-1)に注意 

def gcd(x, y):
  if x > y:
    return gcd(y, x)
  while x != 0:
    x, y = y % x, x
  return y
def lcm(x, y):
  return (x*y)//gcd(x, y)

a, b, c, d = map(int, input().split())
bx = b - (b//c + b//d - b//lcm(c, d))
ax = (a-1) - ((a-1)//c + (a-1)//d - (a-1)//lcm(c, d))
print(bx-ax)