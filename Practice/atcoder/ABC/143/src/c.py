# いろいろやりかたありそうだけど尺取っぽくやってみた

n = int(input())
s = input()
ans = 0
l, r = 0, 0
while l < n:
    while r < n and s[l] == s[r]:
        r += 1
    if r <= l:
        r = l + 1
    ans += 1
    l = r

print(ans)

