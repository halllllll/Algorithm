# 1文字ずつ見てってxを排除するだけですね
x = gets.chomp
s = gets.chomp
ans = ""
s.chars.each do |c|
  if c != x
    ans += c
  end
end
puts ans