s = input()
ans = []
for x in s:
    if x == "0" or x == "1":
        ans.append(x)
    else:
        if len(ans) > 0:
            ans.pop()
print("".join(ans))
