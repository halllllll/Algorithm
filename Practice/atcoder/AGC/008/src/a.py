# 0<x<yだとインクリメント、などのような分岐
# +2は二回反転してる

x, y = map(int, input().split())
if 0<=x<y:
  print(y-x)
elif y<x:
  print(min(2+abs(x-y), 1+abs(-x-y)))
else:
  print(min(abs(y-x), 1+abs(-y-x)))