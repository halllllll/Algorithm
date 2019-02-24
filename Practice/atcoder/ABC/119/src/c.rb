# 小さい順に埋めていく
# 足して絶対値が少なくなる（オーバーしたら差のぶん減らす、足りなかったら差のぶん加えるor再度べつのを加える）
# いや N<=8だし、昇順にソートして組み合わせをとってくるとか
# 組み合わせ、いくつとるかがわかりくい

n, a, b, c = gets.chomp.split.map(&:to_i)
abc = [a, b, c]
arr = []
n.times do
  i = gets.chomp.to_i
  if abc[0] == i
    abc[0] = 0 # is it truely ok zero?
  elsif abc[1] == i
    abc[1] = 0
  elsif abc[2] == i
    abc[2] = 0
  else
    arr << i
  end
end
arr.sort!
p abc.reverse!
p arr

abc.each do |l|
  next if l.zero?
  min_abs = 10**5
  ij_set = []
  # 合体させる
  (0...(arr.size)).to_a.each do |i|
    (i...(arr.size)).to_a.each do |j|
      next if i==j
      tmp_min_abs = min_abs
      # 差を取ったものと最小値比較
      tmp_min_abs = [tmp_min_abs, (l-(arr[i]+arr[j])).abs].min
      if tmp_min_abs < min_abs
        # 選ばれしiとjを保存
        ij_set = [i, j]
        min_abs = tmp_min_abs
      end
    end
  end
  # 合体させない
  arr.each do |ai|
    tmp_min_abs = min_abs
    tmp_min_abs = [tmp_min_abs, (l-arr[ai]).abs].min
    if tmp_min_abs < min_abs
      # 選ばれしiを保存
      ij_set = [i]
      min_abs = tmp_min_abs
    end
  end

end