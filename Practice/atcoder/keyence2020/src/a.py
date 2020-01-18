# max(h, w)でmin(h, w)の方向に塗りまくる
h, w, n = [int(input()) for _ in range(3)]
x, i = 0, 0
while x < n:
    x += max(h, w)
    i += 1
print(i)
