# 最初と最後にAがくるときとAのみからなるとき注意する  (最初の連続するやつ+最後の連続するやつ)*(N-1)がある（+最初の連続するやつ+最後の連続するやつ）
# それ以外は適当にSだけみてN回繰り返す
import math

n = int(input())
s = input()
start_seq = s.find("B")
end_seq = s[::-1].find("B")

if start_seq == -1 or end_seq == -1:
    # Aのみからなる
    # これ間に合うんか? -> 間に合いませんでした
    # print(sum([i + 1 for i in range(n * len(s))]))
    # パクリ 数列の和の公式

    print(((len(s) * n) * (len(s) * n + 1)) // 2)
elif start_seq == 0 or end_seq == 0:
    # 最初と最後がBから始まる->つながらない
    # 単にSをみてN回繰り返すだけ
    arr = [0 for _ in range(len(s) + 1)]
    for i in range(len(s)):
        if s[i] == "A":
            arr[i + 1] = arr[i] + 1
    print(n * sum(arr))
else:
    # 冒頭米参照
    # print(start_seq, end_seq)
    seq = start_seq + end_seq
    sa = sum([i for i in range(1, start_seq + 1)])
    se = sum([i for i in range(1, end_seq + 1)])
    sm = s[start_seq:-end_seq]
    arr = [0 for _ in range(len(sm) + 1)]
    for i in range(len(sm)):
        if sm[i] == "A":
            arr[i + 1] = arr[i] + 1
    # print(arr)
    # print(sa, se, sum([i for i in range(1, seq + 1)]))
    print(n * sum(arr) + sa + (n - 1) * sum([i for i in range(1, seq + 1)]) + se)

