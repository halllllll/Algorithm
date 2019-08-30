# ソートしたやつを小さいやつから書き換えたら嬉しいが、書き換えた結果小さくならないようにする
# bを何枚まで選ぶかはにぶたんで、比較は予め累積和をとっておいたもので
# 配列、更新していくってのを誤読して数分溶かした（それぞれのうちいずれかを取ったときの最大かと思ってた）
# とやったらTLEなった


# え？これふつうにシミュじゃねぇの？ソートしたやつを毎回b個取ってmaxを更新すればいいだけでは

n, m = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))), reverse=True)

for _ in range(m):
    b, c = map(int, input().split())

