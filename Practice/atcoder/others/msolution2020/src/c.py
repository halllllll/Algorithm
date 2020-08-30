from string import ascii_lowercase

n = int(input())
s = list(input())
q = int(input())
ai = {c: i for i, c in enumerate(ascii_lowercase)}
t = [[0 for _ in range(n + 1)] for _ in range(len(ascii_lowercase))]

for i in range(n):
    t[ai[s[i]]][i + 1] = t[ai[s[i]]][i] + 1
for tv in t:
    print(tv)

for _ in range(q):
    query = input().split()
    if int(query[0]) == 1:
        i, c = int(query[1]) - 1, query[2]
        t[ai[s[i]]][i + 1] -= 1
        t[ai[c]][i - 1] += 1
    else:
        l, r = int(query[1]), int(query[2])
        ans = 0
        for c in ascii_lowercase:
            ans += t[ai[c]][r] - t[ai[c]][l - 1]
        print(ans)
