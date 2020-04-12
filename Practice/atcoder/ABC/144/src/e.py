# わからんだろこれ 降順ソート*昇順ソートからの発想が浮かばず
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
l, r = -1, 10**12 + 1  # ちゃんと「取りうることがないもののうち最大値」「取りうることのない最小値」でやる.....

while r - l > 1:
    mid = (r + l) // 2  # 最大値これをめざす
    cur = 0
    for i in range(n):
        if a[i] * b[i] <= mid:
            # Kを使う必要がない
            pass
        else:
            # Kからどんくらい使うか これむずくない？
            cur += a[i] - mid // b[i]
    if cur > k:
        l = mid
    else:
        r = mid
print(r)