s = sorted(input())
if s[0] == s[1] and s[2] == s[3] and len(set(s)) == 2:
    print("Yes")
else:
    print("No")
