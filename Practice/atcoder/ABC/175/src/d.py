n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = -10**18
group_id = 0
group_ids = [-1] * n
groups = {}
# とりあえずグループ分けはできそう（せいぜいNなので）
for i in range(n):
    j = i
    group = []
    group_loop_score = 0
    while group_ids[j] == -1:
        group.append(j)
        group_ids[j] = group_id
        j = p[j] - 1
        group_loop_score += c[j]
    if len(group) > 0:
        groups[group_id] = [group_loop_score, group]
        group_id += 1

for gid, gsets in groups.items():
    if gsets[0] < 0:
        # 一周する前にK回以下で探索を断ち切ったほうがいい
        # ちょい無理やりくさいけど倍した長さの累積和を使ってスタートとゴールを決めてN^2
        tmp_arr = gsets[1] * 2
        tmp_arr_length = len(gsets[1]) * 2
        tmp_ruiseki = [0] * (tmp_arr_length + 1)
        for i in range(1, tmp_arr_length + 1):
            tmp_ruiseki[i] = c[p[tmp_arr[i - 1]] - 1] + tmp_ruiseki[(i - 1)]
        tmp = gsets[0]
        for i in range(tmp_arr_length):
            for j in range(i + 1, min(tmp_arr_length, i + k + 1)):
                tmp = max(tmp, tmp_ruiseki[j] - tmp_ruiseki[i])
        ans = max(ans, tmp)
    else:
        # Kを一周の長さで割ったあまりぶんの長さ以下で貪欲した最大値を最後に加えるとする
        # 残りの(K-上記あまりぶん)はぜんぶ一周に使う
        kk = k % len(gsets[1])
        tmp_arr = gsets[1] * 2
        tmp_arr_length = len(gsets[1]) * 2
        tmp_ruiseki = [0] * (tmp_arr_length + 1)
        for i in range(1, tmp_arr_length + 1):
            tmp_ruiseki[i] = c[p[tmp_arr[i - 1]] - 1] + tmp_ruiseki[i - 1]
        max_rest = 0  # どっかで正になるので0スタートにしとくわ
        for i in range(tmp_arr_length):
            for j in range(i + 1, min(tmp_arr_length, i + kk + 1)):
                max_rest = max(max_rest, tmp_ruiseki[j] - tmp_ruiseki[i])
        ans = max(ans, max_rest + gsets[0] * (k // len(gsets[1])))
print(ans)