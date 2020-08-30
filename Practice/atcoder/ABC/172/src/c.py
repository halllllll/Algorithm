n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
for i in range(1, m + 1):
    b[i] += b[i - 1]

ans = 0
for i in range(len(a)):
    rest = k - a[i]
    if rest < 0:
        break
    left, right = -1, len(b)
    while right - left > 1:
        mid = (left + right) // 2
        if rest - b[mid] >= 0:
            left = mid
        else:
            right = mid
    # print(f"{rest}を越えない最大のBiは{b[left]}")
    ans = max(ans, i + left)
print(ans)