# にぶたん * 2
from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ok, ng = 10 ** 9 + 1, -(10 ** 9) + 1
idx = 0
while ok - ng > 1:
    x = (ok + ng) // 2
    print("now ok,ng,x = {}, {}, {}".format(ok, ng, x))
    total = 0
    for i, p in enumerate(arr):
        if i == idx:
            continue
        total += bisect_right(arr, x // p)
    idx += 1
    print(total)
    if total >= k:
        ok = x
    else:
        ng = x + 1

print(ok)
