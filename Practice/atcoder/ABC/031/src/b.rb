l, h = gets.chomp.split.map(&:to_i)
n = gets.chomp.to_i
n.times do
  x = gets.to_i
  if (l..h).include?(x)
    puts 0
  elsif h < x
    puts -1
  else
    puts l - x
  end
end