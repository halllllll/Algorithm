# じつは尺取でやらなくてもよかったというやつ
n, k = map(int, input().split())
if k == 1:
    print(n)
    exit()
arr = [int(input()) for _ in range(n)]
ans = 0
idx = 1
tmp_length = 1
while idx < n:
    if arr[idx - 1] < arr[idx]:
        tmp_length += 1
    else:
        ans += tmp_length - k + 1 if tmp_length >= k else 0
        tmp_length = 1
    idx += 1
ans += tmp_length - k + 1 if tmp_length >= k else 0
print(ans)
