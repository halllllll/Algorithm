e = set(list(map(int, input().split())))
b = int(input())
l = set(list(map(int, input().split())))
if l == e:
    print(1)
elif l - e == {b}:
    print(2)
elif len(l & e) == 5:
    print(3)
elif len(l & e) == 4:
    print(4)
elif len(l & e) == 3:
    print(5)
else:
    print(0)

