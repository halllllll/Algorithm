s = gets.chomp
doremi = "WBWBWWBWBWBW".chars
case s[0, doremi.size].chars
when doremi
  puts "Do"
when doremi.rotate!(2)
  puts "Re"
when doremi.rotate!(2)
  puts "Mi"
when doremi.rotate!(1)
  puts "Fa"
when doremi.rotate!(2)
  puts "So"
when doremi.rotate!(2)
  puts "La"
when doremi.rotate!(2)
  puts "Si"
end