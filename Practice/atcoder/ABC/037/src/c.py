# N<=10^50だしふつうにやっても間に合うのでは？？？
# と思ったがふつうにやるところでsumのぶんK回回すのが無駄ってことに気づく
# ので、単に累積和のあぶれたぶぶんを引く変形と考える

n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] += arr[i - 1]

ans = 0
j = -1
for i in range(n):
    if i < k - 1:
        continue
    if j == -1:
        ans += arr[i]
    else:
        ans += arr[i] - arr[j]
    j += 1

print(ans)
