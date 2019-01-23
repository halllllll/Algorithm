arr = []
10.times do
  arr << gets.to_i
end
arr = arr.sort.reverse
(0..2).each do |i|
  puts arr[i]
end