# ベン図的にみると赤と青の両方にかかれているやつは考えなくていい（+1円-1円なので）
# と思ったけど複数枚に同じのが書かれている場合があるなこれ
# なので辞書でカウントしつつリストとってxnor
# と思ったけど問題文よく読んだら最悪でも0とれるので青を基準に考えればいいだけだった
blues = {}
for _ in range(int(input())):
    r = input()
    if r in blues:
        blues[r] += 1
    else:
        blues[r] = 1
reds = {}
for _ in range(int(input())):
    b = input()
    if b in reds:
        reds[b] += 1
    else:
        reds[b] = 1

ans = 0
for k, v in blues.items():
    if k in reds:
        ans = max(ans, blues[k] - reds[k])
    else:
        ans = max(ans, v)

print(ans)
