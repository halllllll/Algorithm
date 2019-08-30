# すげぇこんがらがるのでまずは落ち着く
# Cを使う場合とC"だけ"を遣う場合と使わない場合で分ける
a, b, c, x, y = map(int, input().split())
t = (x - y) * a if x > y else(y - x) * b
print(min(a * x + b * y, 2 * c * min(x, y) + t, 2 * c * max(x, y)))
