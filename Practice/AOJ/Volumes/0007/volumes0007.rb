n = gets.to_i

money = 100000
until n.zero?
  money += (((money*0.05)/1000).ceil)*1000
  n-=1
end

puts money