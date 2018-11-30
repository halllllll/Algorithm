# [500, 100, 50, 10]

limit = 15
target = 1000

# 合計がtargetになる組み合わせに等しい
# x, y, z, wとして500x + 100y + 50z + 10w = 1000
ans = 0
(limit+1).times do |x|
  break if target < 500*x
  (limit-x+1).times do |y|
    break if target < (500*x + 100*y)
    (limit - (x+y)+1).times do |z|
      break if target < (500*x + 100*y + 50*z)
      (limit - (x+y+z)+1).times do |w|
        break if target < (500*x + 100*y + 50*z + 10*w)
        next if (500*x + 100*y + 50*z + 10*w) < target
        puts "500*#{x} + 100*#{y} + 50*#{z} + 10*#{w}"
        ans += 1
      end
    end
  end
end

puts ans

# smart flavor
# ------- censored  -------