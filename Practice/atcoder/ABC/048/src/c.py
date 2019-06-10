# 隣り合う2個というが、頭からみていったときに前のやつは流用できないので、あとのやつを優先的に減らしたほうがいい
n, x = map(int, input().split())
arr = list(map(int, input().split()))

cost = 0
for i in range(1, n):
    if arr[i] + arr[i - 1] > x:
        abure = arr[i] + arr[i-1] - x
        if arr[i] >= abure:
            arr[i] -= abure
        else:
          # 足りないぶんはひとつ前からも減らさねばならない
            arr[i - 1] -= abure - arr[i]
            arr[i] = 0
        cost += abure
print(cost)
