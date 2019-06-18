# 最終形態は000..か1111...しかないのでそれぞれ数えて小さい方*2
s = input()
one, zero = 0, 0
for sv in s:
    if sv == "0":
        zero += 1
    else:
        one += 1
print(min(zero, one)*2)
