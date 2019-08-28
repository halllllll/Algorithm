n, x = map(int, input().split())
l = [0] + list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    l[i] += l[i - 1]

for a in l:
    if a <= x:
        count += 1
print(count)
