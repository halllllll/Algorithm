# ん これ微妙にむずくない？
# sの末尾x文字とtの先頭x文字ぶんかぶってるかどうかチェック
n = int(input())
s, t = input(), input()
a = -1
for i in range(n):
    if s[-i - 1 :] == t[: i + 1]:
        a = i
print(len(s) + len(t[a + 1 :]))

