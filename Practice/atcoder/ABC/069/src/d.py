# 問題読んでないけど一行にして折り返して繰り返すみたいなのでいいのでは
h, w = map(int, input().split())
n = int(input())
arr = list(map(int, input().split()))
line = []
for i in range(n):
    line.extend([str(i + 1)] * arr[i])

r = 0
for y in range(h):
    output = line[r : r + w]
    r += w
    if y % 2 == 1:
        print(" ".join(output[::-1]))
    else:
        print(" ".join(output))

