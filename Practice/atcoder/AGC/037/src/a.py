# 前回のやつを保存しつつあたま+1からみていって前回のと同じの場合、長さ1なら更に+1したもの、それ以外は。。。。ありえないので考えなくていい
s = input()
pre = s[0]
ans = 1
idx = 1
# print(pre) 確認用
while idx < len(s):
    if len(pre) == 1:
        if pre != s[idx]:
            ans += 1
            pre = s[idx]
            idx += 1
        else:
            if idx + 1 < len(s):
                # まだ追加できる
                pre = s[idx:idx + 2]
                idx += 2
                ans += 1
            else:
                # 終了
                pre = s[idx - 1:]
                idx += 1
    else:
        # 前回で2文字使っているので今回は1文字でいい
        pre = s[idx]
        ans += 1
        idx += 1
    # print(pre) 確認用
print(ans)
