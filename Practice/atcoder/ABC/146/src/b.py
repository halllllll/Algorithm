from string import ascii_uppercase

n, s = int(input()), input()


def gen(n):
    ret = {k: k for k in ascii_uppercase}
    for i, c in enumerate(ascii_uppercase):
        ret[c] = ascii_uppercase[(i + n) % len(ascii_uppercase)]
    return ret


table = gen(n)
ans = ""
for c in s:
    ans += table[c]
print(ans)
