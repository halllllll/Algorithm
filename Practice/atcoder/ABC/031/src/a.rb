a, d = gets.chomp.split.map(&:to_i)
puts ([a, d].min+1) * ([a, d].max)