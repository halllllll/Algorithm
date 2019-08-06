# 2Lと1Lを基準にして貪欲
q, h, s, d = map(int, input().split())
n = int(input())
arr = [8 * q, 4 * h, 2 * s, d]
x = min(arr)
if n % 2 == 0:
    print((n // 2) * x)
else:
    ans = (n // 2) * x
    ans += min([4 * q, 2 * h, s])
    print(ans)
