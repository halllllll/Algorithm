# 1つだけaであとはa-1個
# a, b = map(int, input().split())
# if b <= a:
#     print(1)
# else:
#     cur = a
#     c = 1
#     while cur < b:
#         c += 1
#         cur += a - 1
#     if cur -
#     print(c)
# なぜかダメなので愚直
a, b = map(int, input().split())
c = 0
cur = 1
while True:
    if cur >= b:
        break
    cur += a - 1
    c += 1
print(c)
