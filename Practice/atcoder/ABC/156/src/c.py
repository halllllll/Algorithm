n = int(input())
arr = list(map(int, input().split()))
ans = 10 ** 18

for i in range(100):
    tmp = 0
    for j in range(n):
        tmp += (arr[j] - (i + 1)) ** 2
    ans = min(tmp, ans)
print(ans)
