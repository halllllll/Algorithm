# 何回目のアタックだよこれ（前回までのは当然読んですら無い）
# 単純にa<bのとき貯めれるだけためて残りをbにぶっこむのじゃ駄目なの?
k, a, b = map(int, input().split())
if a >= b or b - a <= 2:
    # 貯めるだけムダなので全振り
    print(1 + k)
    exit()
x = a  # はじめてa枚貯まってから1円に交換したターン
d = k - x  # x時点での残りターン

if d == 0:
    # 変えないほうがよかったね
    print(1 + k)
    exit()
if d % 2 == 0:
    # 直前で止めて+1したほうがいい
    print(a + (b - a) * (d // 2) + 1)
else:
    # そのまま交換したほうがいい
    print(b + (b - a) * (d // 2))
