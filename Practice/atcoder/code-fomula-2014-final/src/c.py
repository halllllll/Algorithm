# なんかだるそうなのでPythonでやる
# 思ったとおりだるい 超雑に書いた
s = input().split()
ans = set()
for c in s:
    if len(c) == 1 or "@" not in c:
        continue
    r = 0
    for l in range(len(c)):
        if list(c)[l] != "@":
            continue
        else:
            r = l + 1
            while r < len(c) and list(c)[r] != "@":
                r += 1
            if len(set(c[l:r])) == 1:
                # @だけの場合だと思う多分
                pass
            else:
                tmp = ""
                for x in c[l + 1:r]:
                    if x != "@":
                        tmp += x
                    else:
                        if len(tmp) > 0:
                            ans.add(tmp)
                        tmp = ""
                if len(tmp) > 0:
                    ans.add(tmp)
ans = sorted(list(ans))
for a in ans:
    print(a)
