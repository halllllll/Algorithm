# わからん Dを保存しといてK回やっても間に合いそう どうやるかはわからん
# s < tのときはできるだけ大きく動いても構わんのでそうする
# s > tのときはできるだけ左側にいきたいのでそうする
# 最小といいつつ、たとえば右にいきたいときにiが[1, 2]でi+1が[1, 3]の場合はiを無視したいが、最小回数ではなく最小日数なので、どうせ移動しなければならないので移動しておくことに気づく。

n, d, k = map(int, input().split())
ds = []
for _ in range(d):
    ds.append(list(map(int, input().split())))

for _ in range(k):
    s, t = map(int, input().split())
    pos = s
    # print("{}からスタート {}がゴール".format(s, t))
    for i in range(d):
        l, r = ds[i]
        if s < t:
            if l <= pos <= r:
                # print("{}から{}へ移動できるのでそうする".format(pos, r))
                pos = r
                if t <= pos:
                    print(i + 1)
                    break
        elif t < s:
            if l <= pos <= r:
                # print("{}から{}へ移動できるのでそうする".format(pos, l))
                pos = l
                if pos <= t:
                    print(i + 1)
                    break

