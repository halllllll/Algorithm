# 最大値の最小値、ちょうどn/2臭い
# あとは帳尻合わせが効きそう
# 14とかだと7+4+2+1 （7+5+2でも7+4+3でもいい
# かと思いきや 1+2+3+4+5で15いくので, 5+4+3+2でよかった
# 10^7なので毎回足してもどうせ間に合う。これで答えの集合のうち最大値は確定
# あとはそれでnを引いて0になるまで -> これだと間に合わない（pypyだと間に合う）

n = int(input())
ans = []
cur = 0

while cur != n:
    tmp = 0
    for i in range(1, n + 1 - cur):
        if i + tmp >= n - cur:
            tmp = i
            break
        tmp += i
    ans.append(tmp)
    cur += tmp
    # print("tmp = {}, cur = {}".format(tmp, cur))
# print(ans)
for a in ans:
    print(a)
