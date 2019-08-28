a, b = gets.chomp.split.map(&:to_i)
if a < b then
    puts "a < b"
elsif a > b then
    puts "a > b"
else
    puts "a == b"
end