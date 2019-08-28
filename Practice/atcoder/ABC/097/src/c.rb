# k<=5ということは最長で5文字

s = gets.chomp.chars
k = gets.chomp.to_i
result = []

0.upto(s.size-1).each do |i|
  # 1~min(5,s.size)文字
  1.upto([k, s.size-i].min).each do |j|
    result << s[i, j].join("")
  end
end
puts result.uniq.sort[k-1]