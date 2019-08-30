n, k = list(map(int, input().split()))
tree = []
for _ in range(n):
    x = int(input())
    tree.append(x)

tree = sorted(tree)

minimum = 10**9
for i in range(n-k+1):
    minimum = min(minimum, tree[i+k-1] - tree[i])

print(minimum)
