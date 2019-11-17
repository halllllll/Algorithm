# しゃくとり応用

n, k = map(int, input().split())
arr = list(map(int, input().split()))

INF = 10 ** 9
ans = INF

# 愚直にkまでの辞書でいいか -> 間に合いませんでした
# leetcodeのminimum window substringに類題があった
# 必要な文字とその発現箇所だけをフィルタリングしたものを使うらしい
# 辞書でカウントしてやってたけどTLEなるので数値で判定することにする

flag_n = 0

# 文字: 発見されたインデックス
filtered_arr = []
for ai, av in enumerate(arr):
    if av <= k:
        filtered_arr.append([av, ai])

# 探索で発見した文字: カウント
flags = dict([[k, 0] for k in range(1, k + 1)])
r = 0
limit = len(filtered_arr)
for l in range(limit):
    # とりあえず条件が揃うまでrをすすめる
    while r < limit and flag_n < k:
        # 出現したやつ更新
        if flags[filtered_arr[r][0]] == 0:
            flag_n += 1
        flags[filtered_arr[r][0]] += 1
        r += 1
        # print("おかしい 今のflags {}".format(flags))
    # breakしたあとは条件がそろっている
    if flag_n == k:
        # print("l:r= {}:{}".format(l, r))
        # print("実体のl:r = {}:{}".format(filtered_arr[l][1], filtered_arr[r][1]))
        # print(flags)
        # print(arr[filtered_arr[l][1] : filtered_arr[r - 1][1] + 1])
        ans = min(ans, filtered_arr[r - 1][1] - filtered_arr[l][1] + 1)

    if r == l:
        r += 1
    else:
        # lをすすめるので
        if flags[filtered_arr[l][0]] > 0:
            if flags[filtered_arr[l][0]] - 1 == 0:
                flag_n -= 1
            flags[filtered_arr[l][0]] -= 1


print(0 if ans == INF else ans)
