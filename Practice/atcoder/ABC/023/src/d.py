# 復習
# 目標スコアをxとすると hi+si*t <=x を満たすtがある
# t <=(x-hi)/si

n = int(input())
h, s = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    h[i], s[i] = map(int, input().split())

max_score = 10 ** 5 * 10 ** 9


def check(x):
    tmp = []
    for i in range(n):
        if x < h[i]:
            return False
        t = (x - h[i]) // s[i]
        tmp.append(t)
    tmp = sorted(tmp)
    for i in range(n):
        if tmp[i] < i:
            return False
    return True


l, r = 0, max_score
while r - l > 1:
    mid = (r + l) // 2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)