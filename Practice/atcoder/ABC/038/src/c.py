# 単調増加部分の長さをLとしたら∑L個あるので、いけるところまでいけなくなったら計算
n = int(input())
arr = list(map(int, input().split()))
ans = 0
length = 0
for i in range(n):
    if i == 0:
        length = 1
        continue
    if arr[i] > arr[i - 1]:
        length += 1
    else:
        ans += sum(list(range(1, length + 1)))
        length = 1
# 最後に残ってるぶんを足す
ans += sum(list(range(1, length + 1)))
print(ans)
