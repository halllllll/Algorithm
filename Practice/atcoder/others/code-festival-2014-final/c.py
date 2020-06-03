# 問題文の意味が分からんので式を書き出してみる
# 49
# 23 -> 23^1*2 + 23^0*3
# x -> ... + (int(x[-2]+x[-1])^1*x[-1] + x[0]^0*x[0]
# サンプルから最大値が10000000000000000でせいぜい10000なので探索する?<-天才では

n = int(input())
for i in range(10, 10001):
    ans = 0
    target = list(str(i))[::-1]
    for j in range(len(target)):
        ans += (i**j) * int(target[j])
    if ans == n:
        print(i)
        exit()
print(-1)
