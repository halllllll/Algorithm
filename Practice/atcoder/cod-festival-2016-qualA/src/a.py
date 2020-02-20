# 数えていく おしまい
n = int(input())
used = [False for _ in range(n)]
arr = list(map(int, input().split()))
ans = 0
for i, a in enumerate(arr):
    if i + 1 == arr[a - 1]:
        if used[i] == False:
            ans += 1
            used[i] = True
            used[a - 1] = True
print(ans)
