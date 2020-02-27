# 赤が入ってる可能性が0になる場合（すべての球を取り出した場合）があることに注意
n, m = map(int, input().split())
balls = [1 for _ in range(n)]
reddable = [False for _ in range(n)]
reddable[0] = True
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    if reddable[x] == True:
        reddable[y] = True
        balls[x] -= 1
        balls[y] += 1
    else:
        balls[x] -= 1
        balls[y] += 1
    if balls[x] == 0:
        reddable[x] = False

ans = list(filter(lambda x: x == True, reddable))
print(len(ans))
