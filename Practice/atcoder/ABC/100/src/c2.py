# 考察微塵もしてないけど2の約数の数っぽい

n = int(input())
arr = list(map(int, input().split()))
count = 0
for a in arr:
  while a % 2 == 0 and a > 0:
    count += 1
    a //= 2
print(count)