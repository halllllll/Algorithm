# 000~999で決め打ちして数える
# python3だとTLEになるんだけどこれそんなに重いか？？？？？
# pypyだと通った

n = int(input())
s = input()
ans = 0

for i in range(0, 1000):
    t = format(i, "0>3")
    idx = 0
    for c in s:
        if c == t[idx]:
            idx += 1
        if idx == 3:
            ans += 1
            break

print(ans)
