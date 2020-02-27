# わからん
# 本番中、以下のような愚直をやって最後のサンプルをうまく処理できず終了

n, m = map(int, input().split())
arr = sorted(list(set(list(map(int, input().split())))))
brr = list(map(lambda x: x + x // 2, arr))
a = arr[0]  # 公差 14とか
b = brr[0]  # 初項 21とか
ans_lis = [0 for _ in range(m)]

# とりあえず最初のやつをmまで
for i in range(b, m + 1, a):
    ans_lis[i - 1] = 1
# 残りのやつ
for i in range(1, n):
    for j in range(brr[i], m + 1, arr[i]):
        ans_lis[j - 1] += 1

print(ans)
