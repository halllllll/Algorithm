# rr..wwにする します

n = int(input())
c = list(input())
w_count = c.count("W")
if w_count == 0 or w_count == n:
    print(0)
    exit()
ans1 = 0
for i in range(n - 1, n - w_count - 1, -1):
    if c[i] == "R":
        ans1 += 1
print(ans1)
