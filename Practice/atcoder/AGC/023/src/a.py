# スーパーウルトラ激ムズ200点
# A[i]...A[j]の累積和をB[j]-B[i-1]で表すと題意よりB[j]-B[i-1] = 0の箇所を数える
# よってB[j] = B[i-1]となるi,j(i<j)の組の組み合わせの総数となる
# これは適当に2つ選ぶ組み合わせなのでその数がP個あるならP*(P-1)/2でいける

n = int(input())
arr = list(map(int, input().split()))
d = {0: 1}
b = [0]
for i in range(n):
    b.append(b[i] + arr[i])
    if b[i + 1] in d:
        d[b[i + 1]] += 1
    else:
        d[b[i + 1]] = 1
ans = 0
for _, v in d.items():
    ans += (v * (v - 1)) // 2
print(ans)