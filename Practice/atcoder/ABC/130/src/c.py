# 真ん中を通れば必ず二分できてこれが最大値だが、自分自身が真ん中の座標の場合は自分自信を通るどんな直線も二分できる
w, h, x, y = map(int, input().split())
ans1 = (w * h) / 2.0
ans2 = 1 if w / 2 == x and h / 2 == y else 0
print(ans1, ans2)
