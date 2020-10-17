n = int(input())
a = list(map(int, input().split()))
m = list(map(abs, a))
u = sum(map(lambda x: x**2, m))**0.5
t = max(m)
print(sum(m))
print(u)
print(t)