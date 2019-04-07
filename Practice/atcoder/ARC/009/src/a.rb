# 言われた通りにやればいいだけですが何か
n = gets.chomp.to_i
ans = 0
n.times do
  a, b = gets.chomp.split.map(&:to_i)
  ans += a*b
end
puts (ans * 1.05).floor