n = gets.to_i
n.times do
  target = gets.chomp.split.map(&:to_i).sort
  puts target[2]*target[2] == target[1]*target[1] + target[0]* target[0] ? "YES" : "NO"
end
