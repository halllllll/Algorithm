# 貪欲
n, _ = map(int, input().split())
ans = ''.join(list(sorted([input() for _ in range(n)])))
print(ans)
