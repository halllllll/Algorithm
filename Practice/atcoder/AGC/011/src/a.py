# 乗せれるだけ乗っけるのがいいと思うだけなんだけどどうなんでしょう
# なんか実装しにくい 世界一プログラミングが下手
# 二重whileなんてやるからだ forでいいやろ
n, c, k = map(int, input().split())
ans = 0
arr = sorted([int(input()) for _ in range(n)])
cur_passenger = 0
limit = arr[0] + k
for i in range(n):
    if cur_passenger < c and arr[i] <= limit:
        cur_passenger += 1
        # print("{}番目の人は{}のバスに乗せた".format(i, ans))
    else:
        cur_passenger = 1
        limit = arr[i] + k
        ans += 1
        # print("{}番目の人を{}のバスの最初の客にした".format(i, ans))
# あぶれた人を救済
if cur_passenger > 0:
    ans += 1
print(ans)
