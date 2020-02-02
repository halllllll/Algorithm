# 百の位を変えてmax
# と思ったら謎のWA
# あ 各桁試す場合があるのか（思いつかんけど
# は？これでもWA残るんだが？？？？
# 一箇所十の位を*10するの忘れてた

a, b = input().split()
a1 = 900 + 10 * int(a[1]) + int(a[2])
a2 = 100 * int(a[0]) + 90 + int(a[2])
a3 = 100 * int(a[0]) + 10 * int(a[1]) + 9

b1 = 100 + 10 * int(b[1]) + int(b[2])
b2 = 100 * int(b[0]) + int(b[2])
b3 = 100 * int(b[0]) + 10 * int(b[1])
print(max(a1 - int(b), a2 - int(b), a3 - int(b), int(a) - b1, int(a) - b2, int(a) - b3))
