# 1秒で着想したけど実装が一度ドハマリして死亡 死亡ってか殺意
# 考え直して、すべての状態をboolで管理することにした

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
rsp = [True for _ in range(n)]
ans = r if t[0] == "s" else s if t[0] == "p" else p

for i in range(1, n):
    if i + 1 <= k:
        ans += r if t[i] == "s" else s if t[i] == "p" else p
    else:
        if t[i - k] == t[i]:
            if rsp[i - k] == True:
                rsp[i] = False
            else:
                ans += r if t[i] == "s" else s if t[i] == "p" else p
                rsp[i] = True
        else:
            ans += r if t[i] == "s" else s if t[i] == "p" else p
print(ans)
