x = int(input())

# x^5−y^5=(x−y)(x^4+x3^y+x^2y^2+xy^3+y^4)
# x-yをみつける x-y = d[i]


def enum_div(x):
    ret = []
    for i in range(1, x):
        if i * i > x:
            break
        if x % i == 0:
            ret.append(i)
            if i != 1 and i * i != x:
                ret.append(x // i)
    return ret


divs = enum_div(x)

print(divs)
for d in divs:
    for x in range(d):
        y = d - x
        if d * (x**2 + (1 / 2 - (5**0.5) / 2) * x * y +
                y**2) * (x**2 + (1 / 2 + (5**0.5) / 2) * x * y * y**2) == x:
            print("ok")
            print(x, y)
print("omg")
