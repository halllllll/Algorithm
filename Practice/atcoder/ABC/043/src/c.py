# まさかの
# 問題文をちゃんと読もう 文ってか制約
n = int(input())
arr = list(map(int, input().split()))
ans = 10e9
for t in range(-100, 101):
    ans_tmp = 0
    for v in arr:
        ans_tmp += abs(t - v)**2
    ans = min(ans, ans_tmp)

print(ans)
