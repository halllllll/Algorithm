# 言われたとおりにやって数えればいいです
n = gets.chomp.to_i
rc, tc = 0, 0
n.times do
  line = gets.chomp.chars
  line.each do |i|
    if i == "R"
      tc += 1
    elsif i == "B"
      rc += 1
    end
  end
end
if tc>rc
  puts "TAKAHASHI"
elsif tc<rc
  puts "AOKI"
else
  puts "DRAW"
end