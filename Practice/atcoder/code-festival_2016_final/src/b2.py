# 解説を観たのでそれをやってみるバージョン
# （最初に解いたやつは愚直に毎回最大値を求めていた（なんかしらんけど通った））
n = int(input())
cur = 0
target = 0
for i in range(1, n + 1):
    if i + cur >= n:
        target = i
        break
    cur += i

remove_num = sum([i for i in range(1, target + 1)]) - n
for i in range(1, target + 1):
    if i != remove_num:
        print(i)

