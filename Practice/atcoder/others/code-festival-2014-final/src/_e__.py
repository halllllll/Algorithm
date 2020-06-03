# 頭から貪欲でよさそう（しらんけど）
# いらない数を数える
n = int(input())
r = list(map(int, input().split()))
ans1, ans2 = 0, 0
for i in range(1, n - 1):
    if r[i - 1] <= r[i] <= r[i + 1]:
        ans1 += 1
    if r[i - 1] >= r[i] >= r[i + 1]:
        ans2 += 1
print(ans1, ans2)
print(min(n - ans1, n - ans2))
