# 累積和してXを越えるところまでいったら、そこまでの数の組み合わせで達成できる
# （ことがエスパーでわかる）
# TLEなったけど1WAなんで1かなこれ
# 配列は使わないことにする
X = int(input())
n = 0
c = 0
while True:
    if n >= X:
        break
    else:
        c += 1
        n += c

print(c)
