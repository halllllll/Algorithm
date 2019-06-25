# 一番でかいやつは他のやつすべてを吸収できる
# -> i番目において自分より低いやつはすべて吸収できる
# なのでソートして考える
# 自分より高いやつらについては、自分より低いやつをすべて吸収した大きさの
# 2倍以下のやつは吸収できるのでまずそれを求め、
# 自分より大きいものについてそれを適用アンド更新していって最後までいけば生き残れる
# 累積和でもっておく
# なぜかうまくいかない

n = int(input())
arr = list(sorted(list(map(int, input().split()))))
temp_arr = [0 for _ in range(n + 1)]
for i in range(n):
    temp_arr[i + 1] = arr[i] + temp_arr[i]
ans = 1  # 最大のやつ
for i in range(n):
    me = temp_arr[i]
    print(i, me)
    j = i
    while j < n-1:
        if arr[j] <= me * 2:
            me += arr[j]
            j += 1
        else:
            break
    if j == n - 1:
        ans += 1
print(ans)
