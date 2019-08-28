# 全探索する
# 範囲はなんかよくわからんけどaiの取り得る範囲らしい。なんかよくわからんけど

n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i)
if arr.uniq.size == 1
  puts 0
  exit
end
ans = 100000000000000000000000
(-100).upto(100).each do |i|
  cost = 0
  arr.each do |j|
    cost += (j-i)**2
  end
  ans = [ans, cost].min
end
puts ans

<<~EOS
this is shit
minimum, maximum = arr.minmax
mid = (minimum+maximum)/2
if mid.odd?
  mid += 1
end
ans = 0
arr.each do |a|
  ans += (a-mid)**2
end
p ans
EOS