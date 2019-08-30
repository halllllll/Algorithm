# 問題文からはふつうに一箇所から全部回れるとしか思えなくないですか?????????
# テストケース1ひどすぎない？

n = int(input())
d, f = [], []
arr = [[] for _ in range(n)]
for i in range(n):
    gets = list(map(int, input().split()))
    if gets[1] > 0:
        for j in range(gets[1]):
            arr[i].append(gets[2+j])

used = [False for _ in range(n)]
start = [0 for _ in range(n)]
end = [0 for _ in range(n)]


time = 0


def rec(i):
    global time
    used[i] = True
    start[i] = time
    if len(arr[i]) > 0:
        for a in arr[i]:
            if used[a-1] is False:
                used[a-1] = True
                time += 1
                rec(a-1)
        time += 1
    else:
        time += 1
    end[i] = time


# テストケース1が罠というかわけわからんので
# 仕方なくすべて訪問するまで続ける もう順番とか知らんわ
while not all(used):
    time += 1
    rec(used.index(False))

for i in range(n):
    print("{} {} {}".format(i+1, start[i], end[i]))
