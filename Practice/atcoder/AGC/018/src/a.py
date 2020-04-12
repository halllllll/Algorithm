# 1が作れれば必ず終了できる
# 1が作れないようなやつはあるか？
# -> 6 18 26 31 40 があったとき、26と31だけで作れそう
# -> 偶奇が揃っていればいい？
# ex) ぜんぶ奇数だと奇数-奇数で偶数が作れるので結局いける？
# 21 29 45 うんいけそう(8を作れば5ができるので21%5=1)（16を作れば5がry）
# ただしサンプル曰くすべてが同じ数の倍数なら無理そう 適当に最初とそれ以外で試せばいいか
# と思ったけど[6 33 45]とかは作れないのでgcdをとって最後まで更新されなかったらアウトとする
# というか奇数だけでも偶数作れるから奇数さえあればいけるか

# これ最悪ですね 10回提出してWAのたびにif追加してる クソ

n, k = map(int, input().split())
arr = sorted(list(set(list(map(int, input().split())))))
n = len(arr)
if arr[0] == 1 or k in arr:
    print("POSSIBLE")
    exit()
if n < 2 or arr[-1] < k:
    print("IMPOSSIBLE")
    exit()


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b


tmp = gcd(arr[0], arr[1])
# あーもうめちゃくちゃだよ
if tmp == 1:
    print("POSSIBLE")
    exit()
flag = True
for i in range(2, n):
    g = gcd(tmp, arr[i])
    if g != tmp or g == 1:
        flag = False
        break
# あーもうめちゃくちゃだよ
if flag and k % tmp != 0:
    print("IMPOSSIBLE")
    exit()

even_flag, odd_flag = False, False
for a in arr:
    if a % 2 == 1:
        odd_flag = True
    else:
        even_flag = True

# あーもうめちゃくちゃだよ
if odd_flag:
    if k % 2 == 0 and not even_flag:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
    exit()

# あーもうめちゃくちゃだよ
if k % 2 == 1:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
