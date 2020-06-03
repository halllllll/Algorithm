from copy import deepcopy

# 全探索でいけるやろ
n = int(input())
a = list(map(int, input().split()))
ans = 0


def f(ret, idx):
    if idx == n:
        yield ret
    else:
        for x in [-1, 0, 1]:
            next_ret = deepcopy(ret)
            next_ret.append(a[idx] + x)
            yield from f(next_ret, idx + 1)


for g in f([], 0):
    res = len(list(filter(lambda x: x % 2 == 0, g)))
    ans += 1 if res > 0 else 0
print(ans)
