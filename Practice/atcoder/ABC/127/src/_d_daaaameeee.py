# 毎回ソートすると間に合わん
# そもそも一番大きいやつは更新されないので、[b,c]についてcで降順ソートしたものを対象にする
# その時点で大きいものに更新されたやつは二度と更新されないので次回以降は省いたものだけ対象にできる
# andにぶたんでどこまでいけるか
import bisect

n, m = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))))
bc = []
for _ in range(m):
    b, c = map(int, input().split())
    bc.append([b, c])

bc = list(sorted(bc, key=lambda x: x[1], reverse=True))
ans = 0

for bci in bc:
    d = bisect.bisect_left(arr, bci[1])
    arr = arr[min(d, bci[0]) :]
    ans += min(d, bci[0]) * bci[1]
print(ans + sum(arr))
