a, b, c, d = gets.chomp.split.map(&:to_f)
if b/a < d/c
  puts "AOKI"
elsif d/c < b/a
  puts "TAKAHASHI"
else
  puts "DRAW"
end