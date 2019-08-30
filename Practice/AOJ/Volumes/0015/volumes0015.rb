over = 100000000000000000000000000000000000000000000000000000000000000000000000000000000
n = gets.to_i
n.times do
  a, b = gets.to_i, gets.to_i
  if a >= over || b >= over || a+b >= over
    puts "overflow"
  else
    puts a+b
  end
end