# 桁DPと思い込んで終了しました
# BFSでいける、というtwを見かけてなるほどとなった
# これは絶対を走査するときわざわざ0から9まで見ているのと、せっかくbfsなのにソートするようにしているので微妙な例だと思われ
# （でもちゃんと間に合った）

from collections import deque
k = int(input())
arr = set()
for i in range(1, 10):
    arr.add(i)

for i in range(1, 10):
    tmp_arr = deque()
    tmp_arr.append(str(i))
    while len(tmp_arr) > 0:
        cur = tmp_arr.popleft()
        arr.add(int(cur))
        if len(cur) == len("3234566667"):
            next
        target = int(cur[-1])
        for i in range(0, 10):
            if abs(target - i) <= 1:
                next_num = cur + str(i)
                if int(next_num) > 3234566667:
                    continue
                tmp_arr.append(next_num)
arr = sorted(arr)
print(arr[k - 1])
