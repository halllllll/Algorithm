# 雑にソートして全探索じゃ駄目なのかな
# yだけソートしたけど駄目っぽい
n = int(input())
reds = []
blues = []
for _ in range(n):
    reds.append(tuple(map(int, input().split())))
for _ in range(n):
    blues.append(tuple(map(int, input().split())))

# y座標降順
reds = sorted(reds, key=lambda x: x[1], reverse=True)
blues = sorted(blues, key=lambda x: x[1], reverse=True)

ans = 0
used_red = [False for _ in range(n)]
for b in blues:
    for i, r in enumerate(reds):
        if used_red[i]:
            continue
        if b[0] > r[0] and b[1] > r[1]:
            # print("青{}と赤{}をセットにする".format(b, r))
            ans += 1
            used_red[i] = True
            break
print(ans)
