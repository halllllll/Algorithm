# 真ん中（両端を除いたN-2本）は小さい方に引っ張られる
# 両端は都度決める感じ
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
for i in range(n - 2):
    ans[i + 1] = min(arr[i], arr[i + 1])
ans[0], ans[n - 1] = arr[0], arr[-1]
print(" ".join(list(map(str, ans))))
