stack = []
loop do
  n = gets
  break if n.nil?
  n = n.to_i
  if n==0
    puts stack.pop
  else
    stack << n
  end
end