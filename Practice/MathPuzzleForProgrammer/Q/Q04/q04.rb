# Your code here!
N = 100
M = 5

ans = 0
def f(current)
  if N <= current
    0
  elsif M < current# 人が足りない場合
    1 + f(current + M)     #この1+がすごい直感に反する
  else
    1 + f(current*2)    # 半分ずつにしていく
  end
end

puts f(1)

# 各1cmからはじめてNまでつなげてみるタイプ
def f2(current)
  if current < 1
    0
  elsif M < current   # 人が足りない場合
    1 + f2(current - M)
  else
    1 + f2(current/2)        # 2培にしていく
  end
end

puts f2(N)

# so smart flavor
# ------- censored -------