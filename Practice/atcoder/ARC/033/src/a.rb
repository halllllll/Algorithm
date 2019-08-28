# ∑(n) が浮かんでくる
n = gets.chomp.to_i
ans = 0
(1..n).to_a.each do |ai|
  ans+=ai
end
p ans
