# なんか雑に書いたらサンプル3通ったしこれでよさそう
n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 1
d = [0] * (n + 10)
d[0] = 3
for i in range(n):
    ans *= d[a[i]]
    d[a[i]] -= 1
    d[a[i] + 1] += 1
    ans %= mod
print(ans)