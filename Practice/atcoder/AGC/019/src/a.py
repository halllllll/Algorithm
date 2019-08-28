# 4*Q < SならQを使ったほうがいいし以下略
q, h, s, d = map(int, input().split())
n = int(input())
x = min(4 * q, 2 * h, s)
if 2 * x <= d:
    ans = n * x
else:
    if n % 2 == 0:
        ans = (n // 2) * d
    else:
        ans = (n // 2) * d + x

print(ans)
