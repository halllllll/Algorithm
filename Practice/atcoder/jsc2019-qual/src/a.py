M, D = map(int, input().split())

def f(m, d):
  d1, d10 = d % 10, d // 10
  return d1 >= 2 and d10 >= 2 and d1 * d10 == m

count = 0
for i in range(1, M+1):
  for j in range(1, D + 1):
    count += 1 if f(i, j) else 0

print(count)  