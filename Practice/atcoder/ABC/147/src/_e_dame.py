# dpでやろうとしたら最初に思いついたやつだと無理だとわかって50分溶かした

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

# dp[h][w] = [red, blue]を保存していく
dp = [[[0, 0] for _ in range(w + 1)] for _ in range(h + 1)]
for y in range(1, h + 1):
    for x in range(1, w + 1):
        dp[y][x][0] = a[y - 1][x - 1]
        dp[y][x][1] = b[y - 1][x - 1]

for d in dp:
    print(d)

print()

for y in range(1, h + 1):
    for x in range(1, w + 1):

        y_1 = [dp[y][x][0] + dp[y - 1][x - 1][0], dp[y][x][1] + dp[y - 1][x - 1][1]]
        y_2 = [dp[y][x][0] + dp[y - 1][x - 1][1], dp[y][x][1] + dp[y - 1][x - 1][0]]
        if abs(y_1[0] - y_1[1]) < abs(y_2[0] - y_2[1]):
            dp[y][x] = y_1
        else:
            dp[y][x] = y_2

for g in dp:
    print(g)

