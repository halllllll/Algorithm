# 条件より、線分は確実に図形の外にあるので、切断する場合、確実に図形のどこかの辺と2の倍数回ぶつかる
# （1回目は図形をぶち破って内に入り、2回目は図形をぶぬけて外へ、3回目はまた内に...という感じ）
# （内->外を経るたびに断片はひとつずつ増える）
# 「ある線分が別の線分と交差するか？」を調べればよさそうなので、このへんのワードをもとにググる
# なんとなく2Dゲームっぽい雰囲気があるのでそこらへん界隈で適当に思いついたワードも加えながらググる
# 参照元: https://qiita.com/ykob/items/ab7f30c43a0ed52d16f2
# これをそのまま書いただけ、あとは全部の辺（線分）について計算してカウント

ax, ay, bx, by = map(int, input().split())
n = int(input())


def check(ax, ay, bx, by, cx, cy, dx, dy):
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
    return tc * td < 0 and ta * tb < 0


count = 0
points = []
for _ in range(n):
    px, py = map(int, input().split())
    points.append((px, py))

cur = points[0]
# 一周したほうがわかりやすいわ
points.append(cur)
for i in range(1, n + 1):
    nex = points[i]
    cx, cy = cur
    dx, dy = nex
    count += 1 if check(ax, ay, bx, by, cx, cy, dx, dy) else 0
    cur = nex
print(count // 2 + 1)
