# そもそもNにいくやつ以外はいらないよねって発想
n, m = gets.chomp.split.map(&:to_i)
a2c, b2c = Array.new(n, false), Array.new(n, false)
m.times do
  a, b = gets.chomp.split.map(&:to_i)
  if b==n
    b2c[a-1] = true
  end
  if a==1
    a2c[b-1] = true
  end
end
n.times do |i|
  if a2c[i] == true && b2c[i] == true
    puts "POSSIBLE"
    exit
  end
end
puts "IMPOSSIBLE"