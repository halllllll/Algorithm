# 最初と最後を保存すれば10*10ぶんもてばよくて単純に探索するというだけのことなのに1時間以上椅子を温めただけだった
n = int(input())
table = [[0 for _ in range(10)] for _ in range(10)]
for i in range(n + 1):
    f, l = i // (1 * 10**(len(str(i)) - 1)), i % 10
    table[f][l] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += table[i][j] * table[j][i]
print(ans)