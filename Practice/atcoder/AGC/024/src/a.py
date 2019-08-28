# 手を動かしていくつかのabcとkで試したら浮かぶ 
# kが大きいけど最後の文字だけみれば偶奇が分かる

a, b, c, k = input().split()
a, b, c = map(int, [a, b, c])
if int(k[-1])%2==0:
  print(a-b)
else:
  print(b-a)

