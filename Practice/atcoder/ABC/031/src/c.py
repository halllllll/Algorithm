# N<=50なので累積和を使って全探索していく感じ
# という雰囲気だったんだけど違うわ

n = int(input())
arr = list(map(int, input().split()))
max_t, max_a = 0, 0
for i in range(n):

    for j in range(n):
        if i == j:
            continue
        tmp_count_t, tmp_count_a = 0, 0
        x, y = i, j
        if i > j:
            x, y = j, i
        for k in range(x, y + 1):
            if k % 2 == 0:
                tmp_count_t += arr[k]
            else:
                tmp_count_a += arr[k]

        if tmp_count_a > max_a:
            max_a = tmp_count_a
            max_t = tmp_count_t
            print("最適解変更: {} 青木p: {}".format(arr[x:y+1], max_a))
    if tmp_count_t > max_t:
        max_t = tmp_count_t

print(max_t)
