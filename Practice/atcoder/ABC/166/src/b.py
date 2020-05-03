n, k = map(int, input().split())
ans = {}
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for aa in a:
        if aa not in ans:
            ans[aa] = True

print(n - len(ans))
