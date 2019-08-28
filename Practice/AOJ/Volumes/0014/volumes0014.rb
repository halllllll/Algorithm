ans = 0
loop do
  d = gets
  break if d.nil?
  d = d.to_i
  wide_d = d
  i = 1
  ans = 0 
  while d < 600
    ans += (d**2)*wide_d
    i+=1
    d = i*wide_d
  end
  puts ans
end
