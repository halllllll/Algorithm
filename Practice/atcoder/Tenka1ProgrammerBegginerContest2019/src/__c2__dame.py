n = int(input())
s = input()
if "#." not in s:
    print(0)
else:
    seq_w = 0
    for i in range(n):
        if s[i] == ".":
            seq_w += 1
        else:
            break
    seq_b = 0
    for i in range(n - 1, -1):
        if s[i] == "#":
            seq_b += 1
        else:
            break
    print(seq_w, seq_b)
    print(min(s.count(".") - seq_w, s.count("#") - seq_b))

