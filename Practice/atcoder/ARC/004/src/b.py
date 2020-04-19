n = int(input())
a = [int(input()) for _ in range(n)]
if n == 1:
    print(a[0])
    print(a[0])
    exit()
max_ans = sum(a)
min_ans = max(a) - (max_ans - max(a)) if max(a) * 2 > max_ans else 0
print(max_ans)
print(min_ans)