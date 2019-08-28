a, b, c = gets.chomp.split.map(&:to_i)
puts (a*b*2+a*c*2+b*c*2)