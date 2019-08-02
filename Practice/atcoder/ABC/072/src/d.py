# 頭から探して見つかったら適当に次のやつと入れ替えりゃいいのでは
# ->なんか4ケースでダメになるのでなんかを見逃してるっぽい
# 無限にわからん

n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(0, n):
    if arr[i] == i + 1:
        if i == n - 1:
            arr[i], arr[0] = arr[i], arr[0]
        else:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        count += 1


print(count)

