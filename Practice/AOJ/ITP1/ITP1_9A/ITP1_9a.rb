word = gets.chomp

c = 0
loop do
    words = gets.chomp
    break if words == "END_OF_TEXT"
    c += words.split.map(&:upcase).select{|w| w==word.upcase}.size
end
puts c