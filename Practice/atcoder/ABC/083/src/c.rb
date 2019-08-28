x, y = gets.chomp.split.map(&:to_i)

count = 0
while x<=y do
  x*=2
  count += 1
end
puts count