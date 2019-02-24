# w, h(w>h)として w-hするごとに1個ずつ正方形ができるので割っていく。w=h=1になったら終了
# w, h = 8, 5 -> 5, 3 -> 3, 2 -> 2, 1
# 「縦と横を入れ替えたものは1つとしてカウント」される

ans = 0
1.upto(1000).each do |y|
  1.upto(y).each do |x|
    i, j = y, x     # 最初これをしてなくてやってたらyが更新されちゃってずっと1のままというバグをやらかしてた
    next if i == j  # これは正方形
    count = 0
    while j >= 1 do
      count += i/j
      i, j = j, (i % j)
    end
    if count == 20
      ans += 1
    end
  end
end

puts ans
