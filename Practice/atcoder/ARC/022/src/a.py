s = input().lower()
i, c, t = False, False, False
for sv in s:
    if sv == "i" and i == False:
        i = True
    elif sv == "c" and i and c == False:
        c = True
    elif sv == "t" and i and c and t == False:
        t = True
print("YES" if all([i, c, t]) else "NO")
