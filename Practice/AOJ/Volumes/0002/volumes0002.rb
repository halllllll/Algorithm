loop do
  target = gets
  break if target.nil?
  s = target.split.map(&:to_i).sum
  keta = 0
  until s==0
    keta+=1
    s/=10
  end
  puts keta
end