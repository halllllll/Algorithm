# やるだけっぽい
n = int(input())
a = []
for _ in range(n):
    get = input()
    a.append([get, "".join(list(reversed(get)))])

a = list(sorted(a, key=lambda x: x[1]))
for aa in a:
    print(aa[0])

