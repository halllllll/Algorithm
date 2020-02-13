# あたまがこんらんする
# 一発でいけるんだろうけどあたまがよわいので条件分岐
# 結局手元で実験してそれっぽいのをでっちあげただけだった 0点

x, y = map(int, input().split())
k = int(input())

if k <= y:
    print(x + k)
else:
    print((x + y) - (k - y))
