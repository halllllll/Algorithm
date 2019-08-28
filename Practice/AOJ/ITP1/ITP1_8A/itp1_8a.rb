s = gets.chomp
table = Hash[*[*'a'..'z'].zip([*'A'..'Z']).flatten]
table.merge!(table.invert)
s.each_char do |c|
    print table.key?(c) ? table[c] : c
end
puts 