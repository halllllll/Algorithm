# いろいろ試したんだけどコツは
# - 尺取法
# - 積は計算するのではなく結果をもっておいて更新していく
# - なんかr==lでr+=1とseki=1する <- 意味がわからん

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
if 0 in arr:
    print(n)
    exit()

length = 0
seki = 1
r = 0
for i in range(n):
    # l = arr[i]
    # r = max(i, r)
    # print("l: {} r: {}".format(i, r))
    # while r < n-1 and seki*arr[r] <= k:
    while r < n and seki*arr[r] <= k:
        # print("seki: {} arr[{}]: ".format(seki, arr[r]))
        seki *= arr[r]
        # print("now seki {}".format(seki))
        r += 1

    length = max(length, r - i)
    #  seki //= l
    seki /= arr[i]
    # seki = max(1, seki)  # 場当たり的す
    # ぎる
    if r == i:  # ????????????????????????
        r += 1
        seki = 1
    # print("{}".format(arr[i:r - i]))
    # print("length: {}".format(length))

print(length)
