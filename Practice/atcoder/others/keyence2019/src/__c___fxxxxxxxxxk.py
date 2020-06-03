# にぶたんの臭いがする
# 変えなくてもいい(A[i]>=B[i])ならそれでいいが、変えなくてはいけないときに備えてプールしておく
# k個まで変えていいとし、探索終了後に余ったやつを、使ったやつ（A[i]-B[i]）を小さい順にならべたもの、に還元して返してやる 還元しきれなかった数は変えなきゃいけないやつなのでkと比較
# でいけるのか？
# 使った数をカウントしていけば途中で切れそう なので余剰分を大きい順にソートして順に使っていくと残ったやつは変える必要がない

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(B) > sum(A):
    print(-1)
    exit()

pre_ans = 0
difs = []
for i in range(N):
    if A[i] > B[i]:
        difs.append(A[i] - B[i])
    elif A[i] < B[i]:
        # 確実にかえなくてはいけないやつ
        pre_ans += 1
difs = sorted(difs, reverse=True)
# print("使っていくぶん: {}".format(difs))
len_difs = len(difs)

l, r = -1, N + 1
while r - l > 1:
    mid = (l + r) // 2
    count = 0  # 借りた数
    tmp = 0  # 使える分
    for i in range(N):
        if A[i] < B[i]:
            if tmp < (B[i] - A[i]):
                # 新たに借りる必要がある
                # print("足りないので借ります {}".format(difs[count]))
                tmp += difs[count]
                count += 1
            tmp -= B[i] - A[i]
            # print("tmp = {}".format(tmp))
        if mid <= count:
            # 使いすぎ問答無用
            # print("使いすぎたので反省")
            l = mid
            break
    if mid > count:
        # print("まだ使える")
        r = mid
print(l + pre_ans)
