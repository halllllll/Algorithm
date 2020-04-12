n, a, b, c, d = map(int, input().split())
s = input()
if c < b:
    if "##" not in s[a:c - 1] and "##" not in s[b:d - 1]:
        print("Yes")
    else:
        print("No")
elif b < d < c:
    # if ".." in s[b:d - 1] and "##" not in s[a:c - 1]:
    if "..." in s[a:c - 1]:
        print("Yes")
    else:
        print("No")
elif b < c < d:
    if ".." in s[b - 1:c - 1] and "##" not in s[b:d -
                                                1] and "##" not in s[a:c - 1]:
        print("Yes")
    else:
        print("No")
else:
    print(0 / 0)
