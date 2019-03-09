# なぜかまったく同じロジックのrubyではWAなったやつ
s = list(input())
count = 1
ans = ""
tmp = s[0]
for i in range(len(s) - 1):
    if s[i + 1] == tmp:
        count += 1
    else:
        ans += "{}{}".format(tmp, count)
        tmp = s[i + 1]
        count = 1

print(ans+"{}{}".format(tmp, count))
