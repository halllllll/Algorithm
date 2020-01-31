# シミュレーションぽい？iとi+1をみて増加か減少か判断して変わったら終了
n = int(input())
arr = list(map(int, input().split()))
ans = 1
state = 0  # 1..増加 -1..減少 0..未確定 みたいな
for i in range(n - 1):
    if state == 0:
        if arr[i] > arr[i + 1]:
            state = -1
        elif arr[i] < arr[i + 1]:
            state = 1
    elif state == 1:
        if arr[i] < arr[i + 1]:
            continue
        elif arr[i] > arr[i + 1]:
            # リセット
            state = 0
            ans += 1
        else:
            continue
    elif state == -1:
        if arr[i] > arr[i + 1]:
            continue
        elif arr[i] < arr[i + 1]:
            # リセット
            state = 0
            ans += 1
        else:
            continue

print(ans)
