n = int(input())
ans = []
while n != 0:
    if int(n % (-2)) == -1:
        ans.append(1)
        n -= 1  # これが不明
    else:
        ans.append(0)
    n /= -2
print(ans)
