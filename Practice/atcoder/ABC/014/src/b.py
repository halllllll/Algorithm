# pythonのビット操作はクソという定評が自分の中にある
# ので、リストを使う
# したらなんかしらんけどWAなったのでキレながらbinする
n, x = map(int, input().split())
arr = list(map(int, input().split()))

x = list(reversed(list(bin(x)[2:].zfill(n))))
ans = 0
for i in range(n):
    ans += arr[i] if x[i] == "1" else 0
print(ans)
