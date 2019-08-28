# 最短距離は当然abs(sx-tx)回x方向とabs(sy-ty)回y方向
# 同じ座標の周囲4マスすべてを使うことになるのでそうする
# 位置関係が判明しているのを利用

sx, sy, tx, ty = map(int, input().split())
difx, dify = abs(tx - sx), abs(ty - sy)
ans = "R" * difx + "U" * dify + "R" + "D" * (dify + 1) + "L" * (difx + 1) + "U"
ans += "U" * dify + "R" * difx + "U" + \
    "L" * (difx + 1) + "D" * (dify + 1) + "R"
print(ans)
