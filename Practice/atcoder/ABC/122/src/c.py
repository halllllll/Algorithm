n, m = map(int, input().split())
s = input()
imos = [0 for _ in range(n)]
for i in range(1, n):
    if s[i-1] == "A" and s[i] == "C":
        imos[i] = imos[i-1]+1
    else:
        imos[i] = imos[i - 1]
for _ in range(m):
    l, r = map(int, input().split())
    if l > 1:
        print(imos[r-1]-imos[l-1])
    else:
        print(imos[r-1])
