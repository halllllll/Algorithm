n, a, b = gets.chomp.split.map(&:to_i)
arr = []
n.times{arr << gets.to_i}

l, r = 0, 10**9+1
while r-l >= 1 do # r-l>1にしてたんだけどダメなのか
  mid = (l+r)/2
  # mid回と仮定して計算
  count = 0
  temp_arr = arr.map{|x|x-mid*b}
  # 体力が残っているやつをA-Bで何回で倒せるかカウント
  # （A>BかつBで叩き済みなので差で殴る）
  temp_arr.each do |x|
    next if x<=0  # 死んでいる
    # ちょうどmid*(a-b)回で倒せない場合はもっかいたたけば倒せる
    count += x%(a-b)>0 ? x/(a-b) + 1 : x/(a-b)
  end
  if mid < count
    # まだ叩けるので増やす
    l = mid +1
  else
    # 叩きすぎたので減らす
    r = mid
  end
end
puts (r+l)/2