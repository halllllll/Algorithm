n = gets.chomp.to_i
arr = []
n.times do
  arr << gets.chomp.to_i
end
arr = arr.sort.reverse
puts arr[0]/2 + arr[1, n-1].sum