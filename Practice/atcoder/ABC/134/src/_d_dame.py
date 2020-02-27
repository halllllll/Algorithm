# 初期状態で半分から向こうは自分自身の値ということで確定
# 後ろからみていく 間に合いそうにないけど間に合う
# いい入れ方は必ず存在する？
# え なんでこれがWAなのかまるでわからん 正解では？？？？？？？

n = int(input())
arr = list(map(int, input().split()))
lis = [0 for _ in range(n)]

for i in range(n, 0, -1):
    # print("i : {}".format(i))
    count = 0
    for j in range(i - 1, n, i):
        # print(j, end=" ")
        if arr[j] == 1:
            count += 1
    lis[i - 1] = count % 2
    # print("i={}時点での結果 count = {} lis = {}".format(i, count, lis))

if lis == arr:
    ans = []
    for i, l in enumerate(lis):
        if l > 0:
            ans.append(i + 1)
    print(len(ans))
    print(" ".join(list(map(str, ans))))
else:
    print(0)
