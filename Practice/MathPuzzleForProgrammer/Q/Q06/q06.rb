# rubyにsetとかはないのか...
c = 0
2.step(10000, 2) do |i|
  visited = []
  x = i*3+1
  loop do
    if x==i
      c+=1
      break
    elsif visited.include?(x)
      break
    end
    visited << x
    x = x.even? ? x/2 : x*3+1
  end
end
puts c
