alphabet = ("A".."F").to_a.zip(Array.new(("A".."F").to_a.size, 0)).to_h
gets.chomp.chars.each{|c| alphabet[c]+=1}
puts alphabet.values.map(&:to_s).join(' ')