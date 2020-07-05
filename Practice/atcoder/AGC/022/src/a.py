from string import ascii_lowercase
alphabets = ascii_lowercase
s = input()
if len(s) < len(alphabets):
    for c in alphabets:
        if c not in s:
            print(s + c)
            exit()
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

# 14253 next 143,  54213 next 5423, 35421 next 4, 43521 next 45
# 右端からみてi-1, iを比較して減少(S[i]>S[i-1])してたらi-1を基準に切り替える
# 切り替えるのは勘だけどi-1より右側でi-1より大きい最小のやつ？
for i in range(len(s) - 1, 0, -1):
    if s[i] > s[i - 1]:
        t = "死"
        for j in range(i, len(s)):
            if s[i - 1] < s[j]:
                t = s[j] if s[j] < t else t
        print(s[:i - 1] + t)
        exit()
