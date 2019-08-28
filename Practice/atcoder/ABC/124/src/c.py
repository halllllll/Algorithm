# 01010101か10101010かなのでどっちもやってみて比較
w, b = 0, 0
s = input()
for i, sv in enumerate(s):
    if i % 2 == 0:
        if sv == "0":
            b += 1
        else:
            w += 1
    else:
        if sv == "0":
            w += 1
        else:
            b += 1

print(min(w, b))
