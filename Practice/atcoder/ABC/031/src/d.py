# n, kが小さいので全探索できそう
K, N = map(int, input().split())
gets = []
for _ in range(N):
  gets.append(list(input().split()))

gets = list(sorted(gets, key = lambda x : int(x[0])))
print(gets)
def g(limit, arr):
  if limit == 0:
    yield arr
  else:
    for i in [1, 2, 3]:
      next_arr = arr[:]
      next_arr.append(i)
      for j in g(limit-1, next_arr):
        yield j

gen = g(K, [])
for x in gen:
  box = gets[:]
  for b in box:
    keep = dict([[str(i), ""] for i in range(1, K+1)])
    for bi in b[0]:
      if len(b[1]) >= x[int(bi)-1]:
        if keep[bi] == "":
          keep[bi] = b[1][:x[int(bi)-1]]
          b[1] = b[1][x[int(bi)-1]:]
        elif keep[bi] == b[1][:x[int(bi)-1]]:
          b[1] = b[1][x[int(bi)-1]:]
    print(keep)