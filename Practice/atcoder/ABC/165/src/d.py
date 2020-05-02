# なんで解けた（しかも本番中に）のかさっぱりわかりませんが
# たぶん愚直に順番に出力する機構を作って
# - 出力がループするのを確認
# - 左側の floor((a*xi)/b)が単調増加なのを確認
# - 右側の a * floor(xi / b) が最初0が続いているので、よくみるとxi==bのときにはじめて1以上になることを確認
# で、その直前、つまり a * floor(xi/b)==0になる最後のxiのときに差が最大になるのでは、と思ってやったらビンゴだった

from math import floor
a, b, n = map(int, input().split())
print(min(floor((a * (b - 1)) / b), floor((a * n) / b)))
