# いやいやいやいやいやいやいや

# え何 もしかして色って最大8色とはどこにもかいてありませ〜〜〜んとかいうオチ？
# > 4人目が「紫色」を選び、5人目が「黒色」を選んだ時、色の種類数は5であり、これは最大値を取る一つの例である
# まじかよ...

n = int(input())
arr = list(map(int, input().split()))
over = 0
collection = [False for _ in range(8)]
for a in arr:
    c = a // 400
    if c >= 8:
        over += 1
    else:
        collection[c] = True
maximum = sum(filter(lambda x: x is True, collection)) + over
minimum = max(1, sum(filter(lambda x: x is True, collection)))
print(minimum, maximum)
