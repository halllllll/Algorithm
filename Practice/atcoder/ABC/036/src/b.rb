n = gets.to_i
table = []
n.times do
  table << gets.chomp.chars
end

(0...n).each do |j|
  line = []
  (n-1).downto(0) do |i|
    line << table[i][j]
  end
  puts line.join("")
end