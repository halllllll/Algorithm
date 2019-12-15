# 逆に考えるんだ
n = int(input())
arr = list(reversed(list(map(int, input().split()))))
ans = [0 for _ in range(n)]
for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        ans[i] = ans[i - 1] + 1

print(max(ans))
