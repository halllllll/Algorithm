# きりみんちゃんの配信をみてたので期待値は分かる
# 素直にTLEくらったので累積和で加減する
# え これでもだめなの
# あほだった sumしてるし
# 単純にみたら 0.5ずつ増えてるのでそうするか
# 1WA...
# N = 1の場合か？


n, k = map(int, input().split())
arr = list(map(int, input().split()))
table = {}
ans = 0
for i in range(1, 1000 + 1):
    table[i] = (i + 1) * 0.5
if n == 1:
    print(table[arr[0]])
    exit()
lis = [0 for _ in range(n)]
lis[0] = table[arr[0]]
for i in range(n - 1):
    if i + 1 < k:
        lis[i + 1] = lis[i] + table[arr[i + 1]]
    else:
        lis[i + 1] = lis[i] + table[arr[i + 1]] - table[arr[i - k + 1]]
    ans = max(ans, lis[i + 1])
print(ans)
