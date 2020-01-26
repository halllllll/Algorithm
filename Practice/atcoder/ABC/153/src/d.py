# なんか適当にdpをこねくりまわす
# （どうしてできたんだろうね)

h = int(input())

dp = {}
dp[1] = 1


def f(x):
    if x in dp:
        return dp[x]
    if x == 1:
        return 1
    tmp = f(x // 2) + 1
    dp[x] = tmp
    tmp += tmp - 1
    return tmp


print(f(h))

