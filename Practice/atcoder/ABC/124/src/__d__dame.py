# 思ったこと
# - 1は潰しても意味がない。0だけをつぶす
# - 連続してなきゃいけない。頭から後ろからなめていくなにかをする
# - 頭からなめていって「とりあえず登場する0は1にする」貪欲を考える
#   - -> 連続して変えられる箇所がK回を越えないよう回数を増減すればいいのでは？？
# 実装がまるでわからんけどなんとなく尺取っぽい感じでやればいいことに気づく

N, K = map(int, input().split())
s = input()
one_seq, zero_seq = False, False
ans = 0
cur = 0
k = 0
first_ones = []
last_zeros = []

# 愚直すぎひんかこれ
if s[0] == "1":
    for i in range(N - 1):
        if s[i] == "1" and one_seq == False:
            one_seq = True
            first_ones.append(i)
        if s[i] == "0" and s[i + 1] == "1":
            one_seq = False
            last_zeros.append(i)
else:
    for i in range(N - 1):
        if s[i] == "0" and zero_seq == False:
            zero_seq = True
            last_zeros.append(i)
        if s[i] == "1" and s[i + 1] == "0":
            zero_seq = False
            first_ones.append(i)

print(first_ones)
print(last_zeros)

