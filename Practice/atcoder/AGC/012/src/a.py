# 3Nを降順に並べると上位1/3が最強で下位1/3が弱い、考えるのは間の1/3だけでいい
# -> なんでこれがWAなの....
# あそうか 4 1 100 14 4 66 31 10 6 4 4 89
# 上位から「1位2位」下位から「3位」なので

n = int(input())
arr = list(sorted(list(map(int, input().split())), reverse=True))
arr = arr[1::2]
arr = arr[:n]
print(sum(arr))
