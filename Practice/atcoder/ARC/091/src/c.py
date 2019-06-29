# 書けばわかる 裏になるのは奇数回訪れる場所
# n or w == 1のとき負数になるのを見抜けず1WA
n, w = map(int, input().split())
print(abs(n*w-(2*n+2*w-4)))
