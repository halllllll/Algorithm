n, t = gets.chomp.split.map(&:to_i)
cost = 100000
n.times do 
  cn, tn = gets.chomp.split.map(&:to_i)
  if tn<=t && cn < cost
    cost = cn
  end
end
puts cost < 10000 ? cost : "TLE"