# m-2n >=0 -> 残ったmを4つずつでひとつのセットが作れる
# m-2n < 0 -> m/2個ぶんだけ作れる
n, m = gets.chomp.split.map(&:to_i)

if m-2*n>=0
  x = m-2*n
  puts n+x/4
else
  puts m/2
end