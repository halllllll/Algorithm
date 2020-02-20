# 塗れるパターンは以下の4通り。条件より、赤と青のどちらかは確実に存在する。
# 1. かぶらない
# 2. 一部かぶる
# 3. 青が赤に完全に含まれる
# 4. 赤が青に完全に含まれる
# 3か4の場合は（赤, 紫), (青, 紫)になるので3,4だけを判定する
# 矩形の中に円が含まれる状態(4)は単純に範囲をみればいいが、その逆の場合は範囲を満たしていても角が円の外側に出てしまう場合がある


import math

x, y, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
if x - r <= x2 <= x3 <= x + r and y - r <= y2 <= y3 <= y + r:
    if (
        math.sqrt(pow(x - x2, 2) + pow(y - y2, 2)) <= r
        and math.sqrt(pow(x - x2, 2) + pow(y - y3, 2)) <= r
        and math.sqrt(pow(x - x3, 2) + pow(y - y2, 2)) <= r
        and math.sqrt(pow(x - x3, 2) + pow(y - y3, 2)) <= r
    ):
        # 完全に含まれる場合 円の中心と各角までの距離がすべてr以下ならok
        print("YES")
        print("NO")
    else:
        # 一部がはみでてる
        print("YES")
        print("YES")
elif x2 <= x - r <= x + r <= x3 and y2 <= y - r <= y + r <= y3:
    print("NO")
    print("YES")
else:
    print("YES")
    print("YES")

