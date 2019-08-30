# ai<=biなので基本的にbiが強い。最強のaiより弱いbiは使う必要がない
# 順番は関係ないので選びぬかれたbiを強いほうか使っていって、倒せなかったら最強のaiをHがなくなるまで使う
# これだとPypyでギリギリ間に合わん...

n, h = map(int, input().split())
a, b = 0, []
for _ in range(n):
    ai, bi = map(int, input().split())
    a = max(a, ai)
    b.append(bi)
b = list(sorted(b))

l, r = 0, n
while r-l > 0:
    mid = (l + r) // 2
    if b[mid] >= a:
        r = mid
    else:
        l = mid + 1
b = b[r:][::-1]
count = 0
for bi in b:
    h -= bi
    count += 1
    if h <= 0:
        break

if h > 0:
    count += h // a if h % a == 0 else h // a + 1

print(count)
