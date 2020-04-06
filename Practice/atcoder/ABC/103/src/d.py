# nいらんな
# -####-------
# ----##------
# --####------
# -----###----
# -------- ##-
# みたいな感じで終端でソートするといい感じに見えてくる
# A[i+1].Left < A[i].Rightの場合かつdivide_pos < A[i].Leftでぶったぎる
# ぶったぎったらdivide_pos更新 更新するときは今のやつの終端-1がいい

_, m = map(int, input().split())
interval = []
for _ in range(m):
    interval.append(list(map(int, input().split())))
interval = sorted(interval, key=lambda x: x[1])
divide_pos = -1
ans = 0
for itv in interval:
    if divide_pos < itv[0]:
        ans += 1
        divide_pos = itv[1] - 1
print(ans)