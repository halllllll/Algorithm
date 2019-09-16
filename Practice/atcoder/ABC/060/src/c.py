# なんかもうこれめちゃくちゃ解きにくい

n, t = map(int, input().split())
arr = list(map(int, input().split()))

x = t
for i in range(n - 1):
    x += min(arr[i + 1] - arr[i], t)
print(x)
