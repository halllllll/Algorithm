a = 1
b = 1
count = 0 
loop do
  break if count >= 5
  ab = (a + b)
  a = b
  b = ab
  next if b <= 144
  s = 0
  loop do
    break if ab.zero?
    s += ab % 10
    ab /= 10
  end
  if (b % s).zero?
    puts b
    count += 1 
  end
end
