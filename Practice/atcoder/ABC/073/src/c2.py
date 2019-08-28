# 最後に残るのは奇数回登場したやつ
n = int(input())
hash = dict()
for _ in range(n):
    x = int(input())
    if x in hash:
        hash[x] += 1
    else:
        hash[x] = 1


ans = 0
for _, v in hash.items():
    if v % 2 == 1:
        ans += 1
print(ans)
