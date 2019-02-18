n = gets.chomp.to_i

if n==0 || n==1
  puts 1
else
  a, b = 1, 1
  while n>0
    n-=1
    a, b = b, a+b
  end
  puts a
end