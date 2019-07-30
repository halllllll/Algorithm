# 解き直し
# 名前にTypicalって書いてあるのでTypicalです


n, m = map(int, input().split())
step_count = [0 for _ in range(n+1)]
ng_step = [False for _ in range(n+1)]
for _ in range(m):
  ng = int(input())
  ng_step[ng] = True

for i in range(n+1):
  if ng_step[i]:
    step_count[i] = 0
  else:
    if i==1:
      step_count[i] = 1
    elif i==2:
      step_count[i] = 1 + step_count[i-1]
    else:
      step_count[i] = (step_count[i-2]+step_count[i-1])%(10**9+7)

print(step_count[-1])