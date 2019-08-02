# 9or8で埋めたやつが強い あるいはオリジナル
# 桁を一つ落として（1なら9999...）残りを9で埋める
# オリジナルはたとえば199とかのとき19が最大になる

s = input()
tmp = 0
for i in s:
    tmp += int(i)
if s[0] == "1":
    print(max(9 * (len(s) - 1), tmp))
else:
    print(max(int(s[0]) - 1 + 9 * (len(s) - 1), tmp))

