# 偶数のこころが生えた
n = int(input())


def f(x):
    ans = 0
    while x % 2 == 0:
        ans += 1
        x //= 2
    return ans


ans = sum(list(map(lambda x: f(int(x)), input().split())))
print(ans)
