n, q = list(map(int, input().split()))
queue = [list(map(lambda x: int(x) if x.isnumeric() else x, input().split()))
         for i in range(n)]
queue.reverse()
c = 0
while True:
    if len(queue) == 0:
        break
    t = queue.pop()
    c += min(t[1], q)
    if t[1] <= q:
        print(t[0], c)
        continue
    t[1] -= q
    queue.insert(0, t)

"""
p2 180
p5 400
p1 450
p3 550
p4 800
"""
