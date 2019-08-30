s = gets.chomp
ss = s.chars.uniq
puts s.size == ss.size ? "yes" : "no"