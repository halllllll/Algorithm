# minより右側にあるmaxの差 * Tすれば最大になる。その差が同じペアは別解としてある
# でもこうするとTの値は意味ないよなぁ
# 「自分より左側で最小の数」「自分より右側で最大の数」の配列を作って、再度頭からなめていけば最大の差とそれをとるペアがわかる

# PyPyだとREなって、Pythonだと2問TLEなる....

n, t = map(int, input().split())
arr = list(map(int, input().split()))
min_arr = [10**9+1 for _ in range(n)]
max_arr = [-1 for _ in range(n)]
now_min, now_max = 10**9+1, -1
for i in range(n):
    if now_min > arr[i]:
        now_min = arr[i]
    min_arr[i] = now_min
    if now_max < arr[-i - 1]:
        now_max = arr[-i-1]
    max_arr[-i - 1] = now_max

max_dif = 0
dif_paris = []
for i in range(n):
    if max_arr[i] - min_arr[i] > max_dif:
        max_dif = max_arr[i] - min_arr[i]
        dif_paris.clear()
        dif_paris.append([max_arr[i], min_arr[i]])
    elif max_arr[i] - min_arr[i] == max_dif:
        if [max_arr[i], min_arr[i]] not in dif_paris:
            dif_paris.append([max_arr[i], min_arr[i]])

print(len(dif_paris))
