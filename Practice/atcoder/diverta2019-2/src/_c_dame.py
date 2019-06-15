# クソザコナメクジ

# 負数を最後まで太らせて、最後に正の数の一番小さいやつに引く（符号がひっくりかえるので加えることになる）
N = int(input())
A = map(int, input().split())
plus, minus = [], []
for a in A:
    if a < 0:
        minus.append(a)
    else:
        plus.append(a)

plus = list(sorted(plus))
minus = list(reversed(sorted(minus)))

ans = 0
ans_list = []

if len(minus) == 0:
    # 太らせる要素がないので正の数から作る
    # 初回 最も小さい数 - 最も大きい数 して最大の負数をつくる
    # あとは残ってるやつから「引く」を加え続けて最後の一回で自らを「引く」
    a, b = plus[0], plus[-1]
    plus = plus[1:-1]
    if len(plus) > 0:
        ans_list.append([a, b])
        ans = a - b
        for p in plus[1:]:
            ans_list.append([ans, p])
            ans -= p
        ans_list.append([plus[0], ans])
        ans = plus[0] - ans
    else:
        ans_list.append([b, a])
        ans = b - a
else:
    # 残りの負数から最大の負数を作る。まず（正方向に）最大 - （正方向に）最小することで最大の正の数がデキるので、
    # あとは（正方向に）最小の一つ前まで 引くを加えていき、最後に逆に自分自身を加える
    if len(minus) == 1:
        ans = minus[0]
    elif len(minus) == 2:
        a, b = minus[0], minus[-1]
        ans_list.append([b, a])
        ans = b - a
    else:
        a, b = minus[0], minus[-1]
        ans = b
        ans_list.append([a, b])
        for m in minus[1:-2]:
            ans_list.append([ans, m])
            ans += m * (-1)
        ans_list.append([minus[-1], ans])
        ans = minus[-1] - ans

    # 正のやつを食う
    for p in plus[1:]:
        ans_list.append([ans, p])
        ans = ans - p
    # 仕上げ
    ans_list.append([plus[0], ans])
    ans = -1 * ans + plus[0]

    # もう1パターンあったわ
    ans_list2, ans2 = [], 0
    ans2 = plus[-1]
    for m in minus:
        ans_list2.append([ans2, m])
        ans2 = ans2 - m
    plus[-1] = ans2

    a, b = plus[0], plus[-1]
    tmp_ans = 0
    plus = plus[1:-1]
    if len(plus) > 0:
        ans_list2.append([a, b])
        tmp_ans = a - b
        for p in plus[1:]:
            ans_list2.append([tmp_ans, p])
            tmp_ans -= p
        ans_list2.append([plus[0], tmp_ans])
        tmp_ans = plus[0] - tmp_ans
    else:
        ans_list2.append([b, a])
        tmp_ans = b - a

    if ans < ans2:
        ans = ans2
        ans_list = ans_list2

print(ans)
for a in ans_list:
    print(a[0], a[1])
