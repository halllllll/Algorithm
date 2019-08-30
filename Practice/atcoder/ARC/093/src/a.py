# 図を書いて整理すればいいですね 差分の配列を利用
n = int(input()) 
a = [0] + list(map(int, input().split())) + [0]
b = [0 for _ in range(n+1)]
for i in range(n+1):
  b[i] = abs(a[i] - a[i+1])

s = sum(b)

for i in range(n):
  print(s - (b[i]+b[i+1]) + abs(a[i+2] - a[i]))
