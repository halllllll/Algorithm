# 並んでるやつから取ったほうがいい + 折返しのぶんは左右どっちにいってから折り返すのがいいかminで判定
# cur, cur + kで調べる
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 10 ** 10
for i in range(n - k + 1):
    if arr[i] < 0 and arr[i + k - 1] < 0:
        ans = min(ans, abs(arr[i]))
    elif arr[i] < 0 and 0 <= arr[i + k - 1]:
        ans = min(
            ans, abs(arr[i]) * 2 + arr[i + k - 1], abs(arr[i]) + arr[i + k - 1] * 2
        )
    elif 0 <= arr[i] <= arr[i + k - 1]:
        ans = min(ans, arr[i + k - 1])

    # print("taken from {}, ans = {}".format(arr[i : i + k], ans))
print(ans)
