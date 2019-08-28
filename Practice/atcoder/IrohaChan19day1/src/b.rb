# 便利メソッド rotate
s = gets.chomp.chars
n = gets.chomp.to_i
s.rotate!(n)
puts s.join