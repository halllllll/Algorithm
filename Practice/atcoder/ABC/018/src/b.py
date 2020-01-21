# REなるのジャッジシステムのバグでは？？？？？？？？？？？？？？

s = list(input())
n = int(input())

for _ in range(n):
    l, r = map(lambda x: int(x) - 1, input().split())
    s = s[:l] + list(reversed(s[l : r + 1])) + s[r + 1 :]
print("".join(s))
