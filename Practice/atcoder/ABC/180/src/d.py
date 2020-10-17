x, y, a, b = map(int, input().split())
ans = 0
xx = x
while x * a - x < b:
    ans += 1
    x *= a
    if x >= y:
        ans -= 1
        break

if y - x > 0:
    ans += (y - x) // b
    if (y - x) % b == 0:
        ans -= 1
# ans2 = 0
# if (y - xx) % b == 0:
#     ans2 = (y - xx) // b - 1
# else:
#     ans2 = (y - xx) // b
# print(max(ans, ans2))
print(ans)
