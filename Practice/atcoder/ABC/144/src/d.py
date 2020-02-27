# 実装と発想がむずいにぶたん
# というか最初は誰でもO(1)を考えるよなこれ にぶたんはむしろ少数派では
# （実際ほかの解答を見たらみーーーんなatan使ってるし）
# でもこれを見た瞬間やるだけと言ってるヒトはちょっとよくわからん

import math

a, b, x = map(int, input().split())

l, r = 0.0, 90.0
if a * b / 2.0 > (x / a):
    # 半分未満の場合
    while l + 10 ** (-8) < r:
        theta = (l + r) / 2.0
        # 限界まで傾けたときの筒を横から見た時、水の入ってる部分はbを対辺とする直角三角形で、底辺をeとすると
        # tan(theta) = b / e -> e = b / tan(theta)
        # よって面積は (e * b)/2
        e = b / math.tan(math.radians(theta))
        s2 = (e * b) / 2.0
        # 比較すべきは台形じゃなくてx/aだった（重要）
        if s2 > (x / a):
            l = theta
        else:
            r = theta
else:
    # 半分以上の場合
    while l + 10 ** (-8) < r:
        theta = (l + r) / 2.0
        # 限界まで傾けたときの筒を横から見た時、水の入っていない部分が直角三角形になる
        # 底辺がaなので、対辺をeとすると、tan(theta) = e/a -> e = a * tan(theta)
        # なので三角形の面積は (a * tan(theta) * a)/ 2
        # 同じくラジアンに変換して渡す
        s2 = (a * math.tan(math.radians(theta)) * a) / 2.0
        if (x / a) + s2 < a * b:
            l = theta
        else:
            r = theta
print(l)
