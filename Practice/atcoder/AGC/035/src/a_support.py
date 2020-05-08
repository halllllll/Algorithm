# 出力して確かめるだけのやつ
n = int(input())
a = list(map(int, input().split()))
for av in a:
    print(f"{bin(av)[2:]:0>10}")
