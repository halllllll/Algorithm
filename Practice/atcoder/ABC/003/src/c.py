# 0の状態からmaxのやつをみてもmax/2にしかならないし、maxを越えることはない
# ので、小さい順にみていけば最後のmaxのときにはなんとなくmaxにギリギリ近づける
# ここまで問題文を読んでなかったので気づかなかったけどNの中からK個えらぶのね
# Kはもちろん大きい順がいい
n, k = map(int, input().split())
r = sorted(list(map(int, input().split())), reverse=True)[:k]
r = list(reversed(r))
ans = 0
for i in range(k):
    ans = (ans + r[i]) / 2
print(ans)
