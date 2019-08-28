# 予め用意しておく
require 'prime'
now = 0
arr = (0..10**5).map do |x|
  if Prime.prime?(x) && Prime.prime?((x+1)/2)
    now+=1
  end
  x = now
end
gets.to_i.times do
  l, r = gets.chomp.split.map(&:to_i)
  puts arr[r]-arr[l-1]
end