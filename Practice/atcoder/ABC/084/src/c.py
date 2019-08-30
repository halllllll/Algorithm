# 基本シミュレーション
# Nが小さいので予めN回の入力を保存しておく方針

n = int(input())
inputs = []
for _ in range(n-1):
    c, s, f = map(int, input().split())
    inputs.append([c, s, f])

for i in range(n - 1):
    current_time = 0
    for data in inputs[i:]:
        c, s, f = data
        if current_time < s:
            # 開通式前なので待つ（始発に乗る）
            current_time = s
        else:
            # すでに開通式を終えて運行が開始されている
            # 次に出る最も速いやつまで待つ
            # c + f * nを満たすnのうちcurrenttimeを超える最小のnを求める
            # にぶたんでええか
            left, right = 0, 10 ** 9
            while left < right:
                mid = (left + right) // 2
                if (s + f * mid) >= current_time:
                    right = mid
                else:
                    left = mid + 1
            # left が n
            current_time = s + f * left
        # 乗車時間
        current_time += c
    print(current_time)
# N番目からN番目には0秒
print(0)
