# にぶたんが失敗したので両端からしゃくとりするような感じでやってみる
# 差分でソートして大きく足りないものは大きく余ってるやつをぶつける

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) < sum(B):
    print(-1)
    exit()
D = []
pre_ans = 0  # 確実に変えなくてはいけないやつ
for i in range(N):
    if A[i] != B[i]:
        D.append(A[i] - B[i])
        if A[i] < B[i]:
            pre_ans += 1
D = sorted(D)

used = 0
tmp = 0
# print(D)
l, r = 0, len(D)
while r - l > 1:
    # print("now tmp: {}".format(tmp))
    if tmp + D[l] < 0:
        # 新たに借りる
        r -= 1
        used += 1
        tmp += D[r]
    tmp += D[l]
    l += 1
print(used + pre_ans)
