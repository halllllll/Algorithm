# 近いほうが嬉しい。xi, yiそれぞれでソートしたものをもっておいて、今いるx, yからそれぞれ直近の場所に移動した場合の小さい方を採用していく
# 値が同じ場合とかの探索がわからん。。。。


class Node:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y


n = int(input())
nodes = []
for i in range(n):
    x, y = map(int, input().split())
    node = Node(i, x, y)
    nodes.append(node)

sorted_by_x = sorted(nodes, key=lambda t: t.x)
sorted_by_y = sorted(nodes, key=lambda t: t.y)

print(list(map(lambda t: [t.key, t.x], sorted_by_x)))
print(list(map(lambda t: [t.key, t.y], sorted_by_y)))


def nibutan(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
