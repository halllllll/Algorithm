# ぜんぶ同じなら永遠に続く あとはわからんからシミュ
# ぜんぶ奇数の場合は-1じゃなくて0

a, b, c = map(int, input().split())
if a == b == c:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        print(-1)
    else:
        print(0)
    exit()

count = 0
while True:
    if len(set(list(map(lambda x: x % 2, [a, b, c])))) != 1:
        break
    count += 1
    a, b, c = b / 2 + c / 2, a / 2 + c / 2, a / 2 + b / 2

print(count)
