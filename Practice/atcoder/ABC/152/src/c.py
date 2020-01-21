# 自分より左側には自分より小さい数しかないよってやつを調べる min更新
n = int(input())
arr = list(map(int, input().split()))
ans = 0
tmp = 10 ** 10
for a in arr:
    if tmp >= a:
        ans += 1
        tmp = min(tmp, a)
print(ans)
