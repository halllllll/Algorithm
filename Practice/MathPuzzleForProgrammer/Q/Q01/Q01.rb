n = 11
loop do
    ans = 
    n.to_s(2) == n.to_s(2).reverse &&
    n.to_s(8) == n.to_s(8).reverse &&
    n.to_s == n.to_s.reverse
    break if ans
    n += 2
end
puts n